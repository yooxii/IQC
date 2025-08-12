from template import *
from TH2837 import *

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QWidget,
    QTableWidgetItem,
    QTreeWidgetItem,
    QFileDialog,
)
from PySide6.QtCore import (
    QIODevice,
    QSettings,
    QIODeviceBase,
    QCoreApplication,
    QRect,
    Qt,
    QObject,
    Signal,
    QSize,
)
from PySide6.QtGui import (
    QPixmap,
    QIcon,
)
import serial
import serial.tools.list_ports


class comDialog(QDialog, Ui_comDialog):
    comConnected = Signal()
    sercom = None
    portname = "COM1"
    portbaud = 115200

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

        self.treeWidget.itemClicked.connect(self.setPageChange)

    def setPageChange(self, item: QTreeWidgetItem, col):
        page = item.text(col)
        if page == "窗口":
            self.WinSets()
        elif page == "数据":
            self.DataSets()
        else:
            print(f"Not page:{page}")

    def WinSets(self):
        self.groupBox.setTitle(self.tr("Window Settings"))

    def DataSets(self):
        self.groupBox.setTitle(self.tr("Data Settings"))
        self.label_times = QLabel(self.tr("Basic magnification"))
        self.verticalLayout_2.addWidget(self.label_times)

        self.hLayou_ls = QHBoxLayout()
        self.label_ls_times = QLabel(self.tr("Ls:"))
        self.label_ls_times.setMaximumWidth(120)
        self.comb_ls_times = QSpinBox()
        self.comb_ls_times.setMinimum(-10)
        self.comb_ls_times.setMaximum(10)
        self.hLayou_ls.addWidget(self.label_ls_times)
        self.hLayou_ls.addWidget(self.comb_ls_times)

        self.verticalLayout_2.addLayout(self.hLayou_ls)


class MainWindow(QMainWindow, Ui_MainWindow):
    counttest = 0
    countcomponent = 0
    counttotal = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sercom = serial.Serial(timeout=1)
        self.comdig = comDialog(self.sercom)
        self.initStatusBar()

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

        # 初始化 QSettings
        self.settings = QSettings(
            QSettings.Format.IniFormat, QSettings.Scope.UserScope, "AcBel", "IQC-TH2837"
        )
        self.readSettings()

        self.setsdig = setsDialog(self.settings)

        if self.actionsets_reconn.isChecked():
            self.sercom = self.comdig.comConnect()

    ############################ 设置 ############################
    def showMoresettings(self):
        self.setsdig.show()
        # print("setsdig!!!")

    def readSettings(self):
        """从文件中加载设置项"""
        self.settings.beginGroup("MainWindow")
        self.actionsets_reconn.setChecked(
            self.settings.value("reconn", False, type=bool)
        )
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
        self.sercom.write(cmds.DISP.PAGEquery())
        page = self.sercom.readline().decode().strip()
        page = re.sub(r"[a-z]+", "", page)
        print(page, end="")

        datas = {}
        times = 0
        while len(datas) < 4:
            if times > 30:
                raise TimeoutError(self.tr("Data acquisition timeout!"))
            if times % 3 == 0:
                self.sercom.write(b"TRIG:SOUR BUS\n")
                _ = self.sercom.readline()
                self.sercom.write(b"TRIG\n")
                datas |= self.dealData(page)
                # time.sleep(0.1)
                self.sercom.write(b"TRIG\n")
                datas |= self.dealData(page)
                if len(datas) >= 4:
                    break
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
            else:
                self.sercom.write(b"TRIG:SOUR INT\n")
                _ = self.sercom.readline()
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
            times += 1

        rowCount = self.tableOutput.rowCount()
        self.tableOutput.insertRow(rowCount)
        itemLs = QTableWidgetItem(str(datas["Ls"]))
        itemLs.setData(Qt.ItemDataRole.UserRole, datas["Ls"])
        itemQ = QTableWidgetItem(str(datas["Q"]))
        itemQ.setData(Qt.ItemDataRole.UserRole, datas["Q"])
        itemRdc = QTableWidgetItem(str(datas["Rdc"]))
        itemRdc.setData(Qt.ItemDataRole.UserRole, datas["Rdc"])
        itemNs = QTableWidgetItem(str(datas["Ns"]))
        itemNs.setData(Qt.ItemDataRole.UserRole, datas["Ns"])
        self.tableOutput.setItem(rowCount, 0, itemLs)
        self.tableOutput.setItem(rowCount, 1, itemQ)
        self.tableOutput.setItem(rowCount, 2, itemRdc)
        self.tableOutput.setItem(rowCount, 3, itemNs)
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
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[0])
            print(dec)
        elif page in ["< LIST SWEEP DISP >"]:
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[1])
            print(dec)
        elif page in ["< TRANS MEAS DISP >", "< TRANS JUDGE DISP >"]:
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[2])
            print(dec)
        else:
            raise IndexError(f"{page}" + self.tr("Not the measurement interface!"))
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
        import pandas as pd
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
