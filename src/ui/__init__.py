from template import *
from TH2837 import *
from customAuto import catuo as cat

import pandas as pd

from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
    QTableWidgetItem,
    QTreeWidgetItem,
    QFileDialog,
    QFontDialog,
)
from PySide6.QtCore import QSettings, QCoreApplication, Qt, Signal
from PySide6.QtGui import QPixmap, QFont
import serial
import serial.tools.list_ports


class comDialog(QDialog, Ui_comDialog):
    comConnected = Signal()
    sercom = None
    portname = "COM1"
    portbaud = 115200
    theme = ""

    def __init__(self, com: serial.Serial):
        super().__init__()
        self.setupUi(self)
        self.sercom: serial.Serial = com
        self.btncomref.clicked.connect(self.comsReflash)
        self.listcom.clicked.connect(self.setPort)

        self.comsReflash()

    def accept(self):
        self.comConnect()
        if self.sercom.is_open:
            mess = QMessageBox()
            mess.setWindowTitle(
                QCoreApplication.translate("MainWindow", "串口连接成功")
            )
            mess.setStandardButtons(QMessageBox.StandardButton.Ok)
            mess.setDefaultButton(QMessageBox.StandardButton.Ok)
            mess.show()
        return super().accept()

    def comConnect(self):
        self.sercom.close()
        self.sercom.port = self.portname
        self.sercom.baudrate = self.portbaud
        if not self.sercom.is_open:
            self.sercom.open()
        self.comConnected.emit()
        return self.sercom

    def setPort(self):
        self.portname = self.listcom.currentItem().text()
        self.portbaud = int(self.combobaud.currentText())

    def comsReflash(self):
        self.listcom.clear()
        for port in list(serial.tools.list_ports.comports()):
            self.listcom.addItem(port.name)
        if self.listcom.count() > 0:
            self.listcom.setCurrentRow(0)


class setsDialog(QDialog, Ui_MoreSetsDialog):
    def __init__(self, settings: QSettings):
        super().__init__()
        self.setupUi(self)

        self.settings = settings
        self.currentFont = None

        self.treeWidget.itemClicked.connect(self.setPageChange)
        self.tbtn_fontfamily.clicked.connect(self.getfont)

        self.setShow()

    def setShow(self):
        self.settings.beginGroup("MainWindow")
        fontfamily = self.settings.value("font_family", "Microsoft YaHei UI", type=str)
        fontsize = self.settings.value("font_size", 14, type=int)
        self.currentFont = QFont(fontfamily, pointSize=fontsize)
        self.edit_fontfamily.setText(fontfamily)
        self.spin_fontsize.setValue(fontsize)
        theme = self.settings.value("theme", self.tr("Light"), type=str)
        self.comb_theme.setCurrentText(theme)
        atw = self.settings.value("always_top_window", False, type=bool)
        self.check_topwin.setChecked(atw)
        self.settings.endGroup()

        self.settings.beginGroup("Data")
        poioff = self.settings.value("decimal_point_offset", [0, 0, 0, 0], type=list)
        poi = [int(x) for x in poioff]
        self.spin_ls.setValue(poi[0])
        self.spin_q.setValue(poi[1])
        self.spin_rdc.setValue(poi[2])
        self.spin_ns.setValue(poi[3])
        timeout_retries = self.settings.value("timeout_retries", 10, type=int)
        self.spin_timeoutretry.setValue(timeout_retries)
        self.settings.endGroup()

    def setPageChange(self, item: QTreeWidgetItem, col):
        page = item.text(col)

    def getfont(self):
        ff = self.edit_fontfamily.text()
        fs = self.spin_fontsize.value()
        ok, font = QFontDialog().getFont(QFont(ff, fs), self)
        self.currentFont = font
        if ok:
            self.edit_fontfamily.setText(font.family())
            self.spin_fontsize.setValue(font.pointSize())

    def getPointOffest(self):
        ret = []
        ret.append(self.spin_ls.value())
        ret.append(self.spin_q.value())
        ret.append(self.spin_rdc.value())
        ret.append(self.spin_ns.value())
        return ret

    def saveSettings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("font_family", self.edit_fontfamily.text())
        self.settings.setValue("font_size", self.spin_fontsize.value())
        self.settings.setValue("theme", self.comb_theme.currentText())
        self.settings.setValue("always_top_window", self.check_topwin.isChecked())
        self.settings.endGroup()

        self.settings.beginGroup("Data")
        self.settings.setValue("decimal_point_offset", self.getPointOffest())
        self.settings.setValue("timeout_retries", self.spin_timeoutretry.value())
        self.settings.endGroup()

        self.settings.beginGroup("Device")
        self.settings.setValue("DISP", self.comb_disp.currentText())
        self.settings.endGroup()

        self.settings.sync()

    def accept(self):
        self.saveSettings()
        return super().accept()


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
        self.actionreset.triggered.connect(self.tableOutput.clearFocus)
        self.cboLs.currentTextChanged.connect(lambda: self.updateUnit(0))
        self.cboRdc.currentTextChanged.connect(lambda: self.updateUnit(2))
        self.cboNs.currentTextChanged.connect(lambda: self.updateUnit(3))

        self.actionsavedatas.triggered.connect(self.saveDatas)
        self.actionreset.triggered.connect(self.reset)
        self.actioncompadd.triggered.connect(self.countComponent)
        self.actionsettings.triggered.connect(self.showMoresettings)

    def initVars(self):
        self.setsdig = None
        self.sercom = serial.Serial(timeout=1)
        self.comdig = comDialog(self.sercom)

        self.counttest = 0
        self.countcomponent = 0
        self.counttotal = 0
        self.pointoffest = [0, 0, 0, 0]
        self.alldata = []
        self.isdarktheme = True
        self.theme = ""
        self.always_top_win = False
        self.font_family = ""
        self.font_size = 14
        self.cur_font = None
        self.timeout_retries = 10

    ############################ 设置 ############################
    def showMoresettings(self):
        if self.setsdig is None:
            self.setsdig = setsDialog(self.settings)
        self.setsdig.show()

        self.setsdig.accepted.connect(self.setSettings)

        # print("setsdig!!!")

    def setAlwaysTopWin(self, on_top: bool):
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
        theme = self.settings.value("theme", self.tr("Light"), type=str)
        if theme == self.tr("Light"):
            self.isdarktheme = False
        elif theme == self.tr("Dark"):
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

    def closeEvent(self, event):
        self.saveSettings()
        self.sercom.close()
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
        self.comStatusText = QLabel(text=self.tr("status:"))

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
        mess.setWindowTitle(self.tr("Warning of Misoperation"))
        mess.setText(self.tr("Should the serial port connection be disconnected?"))
        mess.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        mess.setDefaultButton(QMessageBox.StandardButton.No)
        if mess.exec() == QMessageBox.StandardButton.Yes:
            self.sercom.close()
            self.comStatus()

    ############################ 数据处理 ########################
    def getDatas(self):
        import re
        import time

        page = None
        self.sercom.write(b"DISP:PAGE TJD\n")
        self.sercom.write(b"DISP:PAGE?\n")
        page = self.sercom.readline().decode().strip()
        page = re.sub(r"[a-z]+", "", page)
        print(page, end="")

        datas = {}
        times = 0
        while len(datas) < 4:
            if times >= self.timeout_retries:
                raise TimeoutError(self.tr("Data acquisition timeout!"))
            if times % 3 != 0:
                print("TRIG:SOUR BUS")
                self.sercom.write(b"TRIG:SOUR BUS\n")
                _ = self.sercom.readline()
                # time.sleep(0.1)
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
                print("TRIG")
                self.sercom.write(b"TRIG\n")
                datas |= self.dealData(page)
                if len(datas) >= 4:
                    self.MainstatusBar.showMessage(self.tr("数据获取完成"))
                    break
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
            else:
                print("TRIG:SOUR INT")
                self.sercom.write(b"TRIG:SOUR INT\n")
                datas |= self.dealData(page)
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)

            if len(datas) >= 4:
                self.MainstatusBar.showMessage(self.tr("数据获取完成"))
                break
            times += 1
            self.MainstatusBar.showMessage(
                self.tr("数据获取重试次数:") + f"{times}/{self.timeout_retries}"
            )

        datas_sorted = {}
        datas_sorted["Ls"] = datas["Ls"]
        datas_sorted["Q"] = datas["Q"]
        datas_sorted["Rdc"] = datas["Rdc"]
        datas_sorted["Ns"] = datas["Ns"]

        self.alldata.append(list(datas_sorted.values()))

        rowCount = self.tableOutput.rowCount()
        self.tableOutput.insertRow(rowCount)
        for i, v in enumerate(datas_sorted.values()):
            data = v * 10 ** self.pointoffest[i]
            item = QTableWidgetItem(str(data))
            item.setData(Qt.ItemDataRole.UserRole, data)
            self.tableOutput.setItem(rowCount, i, item)

        self.updateUnit(0)
        self.updateUnit(2)
        self.updateUnit(3)

        self.counttest += 1
        self.counttotal += 1
        if self.counttest >= 5:
            self.counttest = 0
            self.countcomponent += 1
        self.countUpdate()

    def updateUnit(self, col: int):
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

    def dealData(self, page):
        data = self.sercom.readline()
        try:
            data = data.decode().strip()
        except:
            data = str(data)
        if page in ["< LCR MEAS DISP >", "< BIN No. DISP >", "< BIN COUNT DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[0])
            print(dec)
        elif page in ["< LIST SWEEP DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[1])
            print(dec)
        elif page in ["< TRANS MEAS DISP >", "< TRANS JUDGE DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[2])
            print(dec)
        else:
            raise IndexError(f"{page} " + self.tr("Not the measurement interface!"))
        ret = {}
        if "type" in dec.keys():
            if dec["type"] == "Lx":
                ret["Ls"] = dec["dataA"]
                ret["Q"] = dec["dataB"]
            if dec["type"] == "DCR":
                ret["Rdc"] = dec["dataA"]
            if dec["type"] == "TURN":
                ret["Ns"] = dec["dataA"]
        return ret

    def saveDatas(self):
        if self.tableOutput.rowCount() == 0:
            raise IndexError(self.tr("No data can be saved!"))
        import json

        savefile = QFileDialog.getSaveFileName(
            self, self.tr("Save the data as"), filter="*.csv;;*.xlsx;;*.txt;;*.json"
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
        mess.setWindowTitle(self.tr("Reset"))
        mess.setText(self.tr("Should all data be reset?"))
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

    ############################ 计数 ###########################
    def countComponent(self):
        if self.counttest == 0:
            mess = QMessageBox()
            mess.setWindowTitle(self.tr("Count of components"))
            mess.setText(
                self.tr(
                    "The test count is zero, but the component count still increases?"
                )
            )
            mess.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            mess.setDefaultButton(QMessageBox.StandardButton.No)
            if mess.exec() == QMessageBox.StandardButton.No:
                return
        elif self.counttest >= 5:
            pass
        self.counttest = 0
        self.countcomponent += 1
        self.countUpdate()

    def countUpdate(self):
        self.label_countcomponent.setText(str(self.countcomponent))
        self.label_counttest.setText(str(self.counttest))
        self.label_counttotal.setText(str(self.counttotal))

    ########################## 录入数据 #########################
    def p():
        pass
