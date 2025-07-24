from template_ui import *

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
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
)


class comDialog(QDialog, Ui_comDialog):
    com = QSerialPort()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btncomref.clicked.connect(self.comreflash)
        self.comreflash()

    def accept(self):
        if self.comConnect():
            mess = QMessageBox()
            mess.setWindowTitle(
                QCoreApplication.translate("MainWindow", "COM connect success")
            )
            mess.setStandardButtons(QMessageBox.StandardButton.Ok)
            mess.setDefaultButton(QMessageBox.StandardButton.Ok)
            mess.show()
        return super().accept()

    def comConnect(self):
        self.com.setPortName(self.listcom.currentItem().text())
        self.com.setBaudRate(int(self.combobaud.currentText()))
        return self.com.open(QIODevice.OpenModeFlag.ReadWrite)

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
        self.comdig = comDialog()
        self.actioncom.triggered.connect(self.comdig.show)
        self.actiondisconn.triggered.connect(self.comclose)

        # 初始化 QSettings
        self.settings = QSettings(
            QSettings.Format.IniFormat, QSettings.Scope.UserScope, "AcBel", "IQC-TH2837"
        )
        self.readSettings()

        if self.actionsets_reconn.isChecked():
            print(self.comdig.comConnect())

    def readSettings(self):
        self.settings.beginGroup("MainWindow")
        self.actionsets_reconn.setChecked(
            self.settings.value("reconn", False, type=bool)
        )
        self.settings.endGroup()

        self.settings.beginGroup("com")
        comName = self.settings.value("Name", "")
        baudRate = self.settings.value("Baud", 115200, type=int)
        self.comdig.com.setPortName(comName)
        self.comdig.listcom.setCurrentItem(
            self.comdig.listcom.findItems(comName, Qt.MatchFlag.MatchExactly)[0]
        )
        self.comdig.com.setBaudRate(baudRate)
        self.comdig.combobaud.setCurrentText(str(baudRate))
        self.settings.endGroup()

    def saveSettings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("reconn", self.actionsets_reconn.isChecked())
        self.settings.endGroup()

        self.settings.beginGroup("com")
        self.settings.setValue("Name", self.comdig.com.portName())
        self.settings.setValue("Baud", self.comdig.com.baudRate())
        self.settings.endGroup()
        self.settings.sync()

    def closeEvent(self, event):
        self.saveSettings()
        self.comdig.com.close()
        event.accept()

    def comclose(self):
        mess = QMessageBox()
        mess.setWindowTitle(
            QCoreApplication.translate("MainWindow", "COM close warning")
        )
        mess.setText(
            QCoreApplication.translate(
                "MainWindow", "Do you want to close the serial port?"
            )
        )
        mess.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        mess.setDefaultButton(QMessageBox.StandardButton.No)
        if mess.exec() == QMessageBox.StandardButton.Yes:
            self.comdig.com.close()
