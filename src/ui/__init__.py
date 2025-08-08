from template import *
from TH2837 import *

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
    QTableWidgetItem,
    QFileDialog,
)
from PySide6.QtSerialPort import (
    QSerialPort,
    QSerialPortInfo,
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
    qtcom = None
    sercom = None
    portname = "COM1"
    portbaud = 115200

    def __init__(self, com: serial.Serial):
        super().__init__()
        self.setupUi(self)
        # self.qtcom: QSerialPort = com
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
        # self.qtcom.close()
        # self.qtcom.setPortName(self.portname)
        # self.qtcom.setBaudRate(self.portbaud)
        # self.qtcom.open(QIODevice.OpenModeFlag.ReadWrite)
        # self.comConnected.emit()

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


class MainWindow(QMainWindow, Ui_MainWindow):
    counttest = 0
    countcomponent = 0
    counttotal = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qtcom = None
        """QSerialPort()"""
        self.sercom = serial.Serial()
        self.comdig = comDialog(self.sercom)
        self.initStatusBar()

        self.actioncom.triggered.connect(self.comdig.show)
        self.actiondisconn.triggered.connect(self.comClose)
        self.comdig.comConnected.connect(self.comStatus)
        # self.qtcom.errorOccurred.connect(self.comStatus)

        self.btnGetdatas.clicked.connect(self.getdatas)
        self.actionreset.triggered.connect(self.tableOutput.clearFocus)
        self.cboLs.currentTextChanged.connect(lambda: self.updateUnit(0))
        self.cboRdc.currentTextChanged.connect(lambda: self.updateUnit(2))
        self.cboNs.currentTextChanged.connect(lambda: self.updateUnit(3))

        self.actionsavedatas.triggered.connect(self.savedatas)

        # 初始化 QSettings
        self.settings = QSettings(
            QSettings.Format.IniFormat, QSettings.Scope.UserScope, "AcBel", "IQC-TH2837"
        )
        self.readSettings()

        if self.actionsets_reconn.isChecked():
            com = self.comdig.comConnect()
            if isinstance(com, QSerialPort):
                self.qtcom = com
            else:
                self.sercom = com

    ############################ 设置 ############################
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
        self.comStatusText = QLabel(
            text=QCoreApplication.translate("COM", "状态:"),
        )

        comStausLayout.addWidget(self.comStatusText)
        comStausLayout.addWidget(self.comStatusIcon)
        comStatusWidget.setLayout(comStausLayout)

        self.MainstatusBar.addPermanentWidget(comStatusWidget)

    def comStatus(self):
        # 状态栏显示串口状态
        if self.qtcom:
            self.comStatusIcon.setToolTip(self.qtcom.portName())
            if self.qtcom.isOpen():
                self.comStatusIcon.setPixmap(self.comStatusIconOn)
            else:
                self.comStatusIcon.setPixmap(self.comStatusIconOff)
        else:
            self.comStatusIcon.setToolTip(self.sercom.port)
            if self.sercom.is_open:
                self.comStatusIcon.setPixmap(self.comStatusIconOn)
            else:
                self.comStatusIcon.setPixmap(self.comStatusIconOff)

    def comClose(self):
        mess = QMessageBox()
        mess.setWindowTitle(QCoreApplication.translate("COM", "误操作警告"))
        mess.setText(QCoreApplication.translate("COM", "是否断开串口连接？"))
        mess.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        mess.setDefaultButton(QMessageBox.StandardButton.No)
        if mess.exec() == QMessageBox.StandardButton.Yes:
            self.sercom.close()
            self.comStatus()

    ############################ 数据处理 ##########################
    def getdatas(self):
        import re
        import time

        if self.counttest >= 5:
            self.counttest = 0

        page = None
        self.sercom.write(cmds.DISP.PAGEquery())
        page = self.sercom.readline().decode().strip()
        page = re.sub(r"[a-z]+", "", page)
        print(page, end="")

        datas = {}
        times = 0
        while len(datas) < 4:
            if times > 30:
                raise TimeoutError("获取数据超时！")
            if times % 3 == 0:
                self.sercom.write(b"TRIG:SOUR BUS\n")
                _ = self.sercom.readline()
                time.sleep(0.1)
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
            self.countcomponent += 1
        self.label_countcomponent.setText(str(self.countcomponent))
        self.label_counttest.setText(str(self.counttest))
        self.label_counttotal.setText(str(self.counttotal))

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
        data = self.sercom.readline().decode().strip()
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
            print(f"{page}不是测量界面！")
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

    def savedatas(self):
        savefile = QFileDialog.getSaveFileName(
            self, "将数据另存为", filter="*.csv;;*.xlsx;;*.txt;;*.json"
        )
