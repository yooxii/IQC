from template import *
from PySide6.QtWidgets import QMainWindow

import serial


class commandWindow(QMainWindow, Ui_commandWindow):
    def __init__(self, com: serial.Serial):
        super().__init__()
        self.setupUi(self)
        self.com = com

        self.btn_send.clicked.connect(self.sendCommand)

    def sendCommand(self):
        cmd = self.edit_send.text()
        if cmd is None or cmd == "":
            return
        self.textBrowser.append(f">>>{cmd}\\n")
        self.com.write(cmd.encode())
        recv = self.com.readline().decode()
        self.textBrowser.append(f"{recv}")
        self.edit_send.clear()
