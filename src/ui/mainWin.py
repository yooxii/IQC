from template import *
import pandas as pd

from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QHBoxLayout,
    QLabel,
    QWidget,
    QTableWidgetItem,
    QFileDialog,
    QTableWidgetSelectionRange,
)
from PySide6.QtCore import QSettings, Qt, QThread, Signal
from PySide6.QtGui import QPixmap, QFont, QGuiApplication
import serial

from .cmdWin import commandWindow
from .comDlg import comDialog
from .setsDlg import setsDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initVars()
        self.initStatusBar()
        self.initConnect()
        self.initSettings()

    def show(self):
        super().show()
        self.setAlwaysTopWin(self.always_top_win)

    ############################ 初始化 ############################
    def initSettings(self):
        # 初始化 QSettings
        self.settings = QSettings(
            QSettings.Format.IniFormat, QSettings.Scope.UserScope, "AcBel", "IQC-TH2837"
        )
        self.readSettings()

        if self.actionsets_reconn.isChecked():
            self.sercom = self.comdig.comConnect()

        self.loadStyle()

    def initConnect(self):
        self.actioncom.triggered.connect(self.comdig.show)
        self.actiondisconn.triggered.connect(self.comClose)
        self.comdig.comConnected.connect(self.comStatus)

        self.btnGetdatas.clicked.connect(self.getDatas)
        self.btnEnterdatas.clicked.connect(self.enterDatas)
        self.actionreset.triggered.connect(self.tableOutput.clearFocus)
        self.cboLs.currentTextChanged.connect(lambda: self.updateUnit(0))
        self.cboRdc.currentTextChanged.connect(lambda: self.updateUnit(2))
        self.cboNs.currentTextChanged.connect(lambda: self.updateUnit(3))
        self.comb_compno.currentTextChanged.connect(self.setDataRange)
        self.buttonGroup.buttonToggled.connect(self.selectDatas)
        self.comb_compno.currentTextChanged.connect(self.selectDatas)
        self.spin_comprowst.valueChanged.connect(self.selectDatas)
        self.spin_comprowend.valueChanged.connect(self.selectDatas)

        self.actionsavedatas.triggered.connect(self.saveDatas)
        self.actionreset.triggered.connect(self.reset)
        self.actioncompadd.triggered.connect(self.countComponent)
        self.actionsettings.triggered.connect(self.showMoresettings)
        self.actioncmdwin.triggered.connect(self.cmdWinShow)

    def initVars(self):
        self.setsdig = None
        self.sercom = serial.Serial(timeout=1)
        self.comdig = comDialog(self.sercom)
        self.cmdWin = None

        self.counttest = 0
        self.countcomponent = 0
        self.counttotal = 0
        self.pointoffest = [0, 0, 0, 0]
        self.alldata = []
        self.comps_loc = []
        self.comp = []
        self.isdarktheme = True
        self.theme = ""
        self.always_top_win = False
        self.font_family = ""
        self.font_size = 14
        self.cur_font = None
        self.timeout_retries = 10
        self.comptest = 5

    ############################ 设置 ############################
    def showMoresettings(self):
        if self.setsdig is None:
            self.setsdig = setsDialog(self.settings)
        self.setsdig.show()

        self.setsdig.accepted.connect(self.setSettings)

    def setAlwaysTopWin(self, on_top: bool):
        """设置是否将主窗口一直置顶

        Args:
            on_top (bool): True:一直置顶;   False:取消置顶
        """
        if on_top:
            self.windowHandle().setFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        else:
            self.windowHandle().setFlag(Qt.WindowType.WindowStaysOnTopHint, False)
        self.update()

    def setAllFont(self):
        if self.cur_font is None:
            return

        self.setFont(self.cur_font)
        if self.setsdig is not None:
            self.setsdig.setFont(self.cur_font)
            self.setsdig.update()
        if self.comdig is not None:
            self.comdig.setFont(self.cur_font)
            self.comdig.update()
        self.update()

    def loadStyle(self):
        self.setAllFont()
        try:
            if self.isdarktheme:
                with open("qss/dark.qss", "r", encoding="utf-8") as f:
                    self.theme = f.read()
            else:
                with open("qss/Light.qss", "r", encoding="utf-8") as f:
                    self.theme = f.read()
        except:
            self.theme = ""
        self.setStyleSheet(self.theme)
        if self.setsdig is not None:
            self.setsdig.setStyleSheet(self.theme)
            self.setsdig.update()
        if self.comdig is not None:
            self.comdig.setStyleSheet(self.theme)
            self.comdig.update()
        self.update()

    def setSettings(self):
        self.readSettings()
        self.loadStyle()
        self.setAlwaysTopWin(self.always_top_win)

        for col in range(self.tableOutput.columnCount()):
            for row in range(self.tableOutput.rowCount()):
                item = self.tableOutput.item(row, col)
                if item is None:
                    print(row, col)
                    continue
                try:
                    ori_value = self.alldata[row][col]
                except ValueError:
                    continue
                new_value = ori_value * 10 ** self.pointoffest[col]
                item.setData(Qt.ItemDataRole.UserRole, new_value)
            self.updateUnit(col)
            self.update()

    def readSettings(self):
        """读取设置项"""
        self.settings.beginGroup("MainWindow")
        fontfamily = self.settings.value("font_family", "Microsoft YaHei UI", type=str)
        fontsize = self.settings.value("font_size", 14, type=int)
        self.cur_font = QFont(fontfamily, pointSize=fontsize)
        self.actionsets_reconn.setChecked(
            self.settings.value("reconn", False, type=bool)
        )
        self.always_top_win = self.settings.value("always_top_window", False, type=bool)
        theme = self.settings.value("theme", 0, type=int)
        if theme == 0:
            self.isdarktheme = False
        elif theme == 1:
            self.isdarktheme = True
        else:
            settings = QSettings(
                "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
                QSettings.NativeFormat,
            )
            if settings.value("AppsUseLightTheme") == 0:
                self.isdarktheme = True
            else:
                self.isdarktheme = False
        self.settings.endGroup()

        self.settings.beginGroup("com")
        comName = self.settings.value("Name", "")
        baudRate = self.settings.value("Baud", 115200, type=int)
        self.comdig.portname = comName
        item = self.comdig.listcom.findItems(comName, Qt.MatchFlag.MatchExactly)
        if item:
            self.comdig.listcom.setCurrentItem(item[0])

        self.comdig.portbaud = baudRate
        self.comdig.combobaud.setCurrentText(str(baudRate))
        self.settings.endGroup()

        self.settings.beginGroup("Data")
        poioff = self.settings.value("decimal_point_offset", [0, 0, 0, 0], type=list)
        self.pointoffest = [int(x) for x in poioff]
        timeout_retries = self.settings.value("timeout_retries", 10, type=int)
        self.timeout_retries = timeout_retries
        comptest = self.settings.value("component_test_times", 5, type=int)
        self.comptest = comptest
        unit = self.settings.value("unit", ["uH", "-", "Ω", "T"], type=list)
        self.cboLs.setCurrentText(unit[0])
        self.cboRdc.setCurrentText(unit[2])
        self.cboNs.setCurrentText(unit[3])
        self.settings.endGroup()

        self.settings.beginGroup("Device")
        self.settings.value("DISP", "")
        self.settings.endGroup()

    def saveSettings(self):
        """保存设置"""
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("reconn", self.actionsets_reconn.isChecked())
        self.settings.endGroup()

        self.settings.beginGroup("com")
        self.settings.setValue("Name", self.comdig.portname)
        self.settings.setValue("Baud", self.comdig.portbaud)
        self.settings.endGroup()

        self.settings.sync()

    def saveUnitSets(self):
        self.settings.beginGroup("Data")
        unit = []
        unit.append(self.cboLs.currentText())
        unit.append(self.cboQ.currentText())
        unit.append(self.cboRdc.currentText())
        unit.append(self.cboNs.currentText())
        self.settings.setValue("unit", unit)
        self.settings.endGroup()

        self.settings.sync()

    def closeEvent(self, event):
        self.saveSettings()
        self.sercom.close()
        if self.cmdWin:
            self.cmdWin.close()
        event.accept()

    ############################ 状态栏 ##########################
    def initStatusBar(self):
        comStatusWidget = QWidget()
        comStausLayout = QHBoxLayout()
        comStausLayout.setContentsMargins(0, 0, 0, 0)

        self.comStatusIconOn = QPixmap(":/pics/pic/comStatus_on.gif").scaled(
            16, 16, Qt.AspectRatioMode.KeepAspectRatio
        )
        self.comStatusIconOff = QPixmap(":/pics/pic/comStatus_off.gif").scaled(
            16, 16, Qt.AspectRatioMode.KeepAspectRatio
        )
        self.comStatusIcon = QLabel(
            pixmap=self.comStatusIconOff,
        )
        self.comStatusText = QLabel(text=self.tr("状态:"))

        comStausLayout.addWidget(self.comStatusText)
        comStausLayout.addWidget(self.comStatusIcon)
        comStatusWidget.setLayout(comStausLayout)

        self.MainstatusBar.addPermanentWidget(comStatusWidget)

    def comStatus(self):
        # 状态栏显示串口状态
        self.comStatusIcon.setToolTip(self.sercom.port)
        if self.sercom.is_open:
            self.comStatusIcon.setPixmap(self.comStatusIconOn)
        else:
            self.comStatusIcon.setPixmap(self.comStatusIconOff)

    def comClose(self):
        mess = QMessageBox()
        mess.setWindowTitle(self.tr("警告"))
        mess.setText(self.tr("确定断开连接？"))
        mess.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        mess.setDefaultButton(QMessageBox.StandardButton.No)
        if mess.exec() == QMessageBox.StandardButton.Yes:
            self.sercom.close()
            self.comStatus()

    ############################ 数据处理 ########################
    def getDatas(self):
        pass

    def getDatasError(self, err):
        self.MainstatusBar.showMessage(err)
        self.btnGetdatas.setText(self.tr("获取数据"))

    def updateDatas(self, datas):
        self.btnGetdatas.setText(self.tr("获取数据"))

        # 重新排序
        datas_sorted = {}
        datas_sorted["Ls"] = datas["Ls"]
        datas_sorted["Q"] = datas["Q"]
        datas_sorted["Rdc"] = datas["Rdc"]
        datas_sorted["Ns"] = datas["Ns"]

        self.alldata.append(list(datas_sorted.values()))

        rowCount = self.tableOutput.rowCount()
        self.tableOutput.insertRow(rowCount)
        print(datas_sorted)
        for i, v in enumerate(datas_sorted.values()):
            data = v * 10 ** self.pointoffest[i]
            item = QTableWidgetItem(str(data))
            item.setData(Qt.ItemDataRole.UserRole, data)
            self.tableOutput.setItem(rowCount, i, item)
            self.tableOutput.scrollToBottom()

        self.updateUnit(0)
        self.updateUnit(2)
        self.updateUnit(3)

        self.counttest += 1
        self.counttotal += 1
        if self.counttest >= self.comptest:
            self.comps_loc.append([rowCount - self.counttest + 1, self.counttest])
            self.comb_compno.addItem(f"{len(self.comps_loc)}")
            self.counttest = 0
            self.countcomponent += 1
        self.countUpdate()

    def updateUnit(self, col: int):
        """更新单位"""
        import math

        if col == 0:
            unit = self.cboLs.currentText()
        elif col == 2:
            unit = self.cboRdc.currentText()
        elif col == 3:
            unit = self.cboNs.currentText()
        else:
            return

        if "u" in unit:
            rate = 1000000
        elif "m" in unit:
            rate = 1000
        else:
            rate = 1

        for row in range(self.tableOutput.rowCount()):
            item = self.tableOutput.item(row, col)
            if item is None:
                print(row, col)
                return
            try:
                ori_value = float(item.data(Qt.ItemDataRole.UserRole))
            except ValueError:
                return
            data = ori_value * rate
            if data == 0:
                decimals = 1
            else:
                decimals = 5 - int(math.log10(abs(data)))
            if decimals < 0:
                decimals = 0
            item.setText(f"{data:.{decimals}f}")
        self.saveUnitSets()

    def saveDatas(self):
        if self.tableOutput.rowCount() == 0:
            raise IndexError(self.tr("没有数据，无法保存！"))
        import json

        savefile = QFileDialog.getSaveFileName(
            self, self.tr("保存数据为"), filter="*.csv;;*.xlsx;;*.txt;;*.json"
        )
        savedata = []
        for row in range(self.tableOutput.rowCount()):
            row_data = []
            for col in range(self.tableOutput.columnCount()):
                item = self.tableOutput.item(row, col).text()
                row_data.append(item)
            savedata.append(row_data)

        df = pd.DataFrame(savedata)
        if savefile[1] in ["*.csv", "*.txt"]:
            df.to_csv(savefile[0], index=None, header=None)
        elif savefile[1] in ["*.xlsx"]:
            df.to_excel(savefile[0], index=None, header=None)
        elif savefile[1] in ["*.json"]:
            with open(savefile[0], "w") as f:
                json.dump(savedata, f)

    ############################ 重置 ###########################
    def reset(self):
        mess = QMessageBox()
        mess.setWindowTitle(self.tr("重置"))
        mess.setText(self.tr("确定重置数据？"))
        mess.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        mess.setDefaultButton(QMessageBox.StandardButton.No)
        if mess.exec() == QMessageBox.StandardButton.No:
            return
        for _ in range(self.tableOutput.rowCount()):
            self.tableOutput.removeRow(0)
        self.countcomponent = self.counttest = self.counttotal = 0
        self.countUpdate()
        self.comp.clear()
        self.comps_loc.clear()
        self.alldata.clear()
        self.comb_compno.clear()
        self.comb_compno.addItem("-")

    ############################ 计数 ###########################
    def countComponent(self):
        """零件计数"""
        if self.counttest == 0:
            mess = QMessageBox()
            mess.setWindowTitle(self.tr("零件计数"))
            mess.setText(self.tr("测试计数为零，仍然增加零件计数吗？"))
            mess.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            mess.setDefaultButton(QMessageBox.StandardButton.No)
            if mess.exec() == QMessageBox.StandardButton.No:
                return
        elif self.counttest >= self.comptest:
            pass
        rowCount = self.tableOutput.rowCount()
        self.comps_loc.append([rowCount - self.counttest, self.counttest])
        self.comb_compno.addItem(f"{len(self.comps_loc)}")
        self.counttest = 0
        self.countcomponent += 1
        self.countUpdate()

    def countUpdate(self):
        """更新计数UI"""
        self.label_countcomponent.setText(str(self.countcomponent))
        self.label_counttest.setText(str(self.counttest))
        self.label_counttotal.setText(str(self.counttotal))

    ########################## 录入数据 #########################
    def setDataRange(self, text):
        """设置录入数据的范围

        Args:
            text (str): 行数
        """
        if text == "-":
            self.spin_comprowst.setMinimum(0)
            self.spin_comprowst.setMaximum(0)
            self.spin_comprowst.setValue(0)
            self.spin_comprowend.setMinimum(0)
            self.spin_comprowend.setMaximum(0)
            self.spin_comprowend.setValue(0)
            self.tableOutput.clearSelection()
            self.comp.clear()
            return
        print(text)
        ran = self.comps_loc[int(text) - 1].copy()
        ran[0] += 1
        print(ran)
        self.spin_comprowst.setMinimum(ran[0])
        self.spin_comprowst.setMaximum(ran[0] + ran[1] - 1)
        self.spin_comprowst.setValue(ran[0])
        self.spin_comprowend.setMinimum(ran[0])
        self.spin_comprowend.setMaximum(ran[0] + ran[1] - 1)
        self.spin_comprowend.setValue(ran[0] + ran[1] - 1)

    def selectDatas(self):
        if self.comb_compno.currentText() == "-":
            return
        start = self.spin_comprowst.value() - 1
        end = self.spin_comprowend.value() - 1
        if self.rBtnLs.isChecked():
            col = 0
        elif self.rBtnQ.isChecked():
            col = 1
        elif self.rBtnRdc.isChecked():
            col = 2
        else:
            col = 3
        print(start, end, col)
        ran = QTableWidgetSelectionRange(start, col, end, col)
        self.tableOutput.clearSelection()
        self.tableOutput.setRangeSelected(ran, True)
        item = self.tableOutput.item(end, col)
        self.tableOutput.scrollToItem(item)

        self.comp.clear()
        for r in range(start, end + 1):
            it = self.tableOutput.item(r, col)
            self.comp.append(it.text())

    def enterDatas(self):
        from customAuto import AutoEnterData

        print(self.comps_loc)
        print(self.comp)
        ato = AutoEnterData()

        win_poi = self.geometry()
        screen = QGuiApplication.primaryScreen()
        scr_poi = screen.geometry()
        self.move(scr_poi.right() - 50, scr_poi.top())
        ato.singleComponent(self.comp)
        self.setGeometry(win_poi)

    ############################ 其他 ##########################
    def cmdWinShow(self):
        if not self.cmdWin:
            self.cmdWin = commandWindow(self.sercom)
        self.cmdWin.show()
