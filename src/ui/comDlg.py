from PySide6.QtWidgets import QMessageBox, QDialog
from PySide6.QtCore import QCoreApplication, Signal
import serial
import serial.tools.list_ports

from template import *


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
        self.setPort()
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
