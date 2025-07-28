from template import *

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
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


class comDialog(QDialog, Ui_comDialog):
    comConnected = Signal()

    def __init__(self, com: QSerialPort):
        super().__init__()
        self.setupUi(self)
        self.com = com
        self.btncomref.clicked.connect(self.comreflash)
        self.comreflash()

    def accept(self):
        if self.comConnect().isOpen():
            mess = QMessageBox()
            mess.setWindowTitle(
                QCoreApplication.translate("MainWindow", "串口连接成功")
            )
            mess.setStandardButtons(QMessageBox.StandardButton.Ok)
            mess.setDefaultButton(QMessageBox.StandardButton.Ok)
            mess.show()
        return super().accept()

    def comConnect(self):
        self.com.close()
        self.com.setPortName(self.listcom.currentItem().text())
        self.com.setBaudRate(int(self.combobaud.currentText()))
        self.com.open(QIODevice.OpenModeFlag.ReadWrite)
        self.comConnected.emit()
        return self.com

    def comreflash(self):
        self.listcom.clear()
        for port in QSerialPortInfo.availablePorts():
            self.listcom.addItem(port.portName())
        if self.listcom.count() > 0:
            self.listcom.setCurrentRow(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com = QSerialPort()
        self.comdig = comDialog(self.com)
        self.initStatusBar()

        self.actioncom.triggered.connect(self.comdig.show)
        self.actiondisconn.triggered.connect(self.comClose)
        self.comdig.comConnected.connect(self.comStatus)
        self.com.errorOccurred.connect(self.comStatus)

        # 初始化 QSettings
        self.settings = QSettings(
            QSettings.Format.IniFormat, QSettings.Scope.UserScope, "AcBel", "IQC-TH2837"
        )
        self.readSettings()

        if self.actionsets_reconn.isChecked():
            self.comdig.comConnect()

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
        self.comdig.com.setPortName(comName)
        item = self.comdig.listcom.findItems(comName, Qt.MatchFlag.MatchExactly)
        if item:
            self.comdig.listcom.setCurrentItem(item[0])

        self.comdig.com.setBaudRate(baudRate)
        self.comdig.combobaud.setCurrentText(str(baudRate))
        self.settings.endGroup()

    def saveSettings(self):
        """保存设置"""
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("reconn", self.actionsets_reconn.isChecked())
        self.settings.endGroup()

        self.settings.beginGroup("com")
        self.settings.setValue("Name", self.com.portName())
        self.settings.setValue("Baud", self.com.baudRate())
        self.settings.endGroup()
        self.settings.sync()

    def closeEvent(self, event):
        self.saveSettings()
        self.comdig.com.close()
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
        self.comStatusIcon.setToolTip(self.com.portName())
        if self.com.isOpen():
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
            self.comdig.com.close()
            self.comStatusIcon.setPixmap(self.comStatusIconOff)
