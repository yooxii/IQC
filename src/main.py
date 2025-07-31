from PySide6.QtWidgets import QApplication, QMainWindow
from ui import *

import TH2837.cmds as cmds


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


# def main():
#     ser = serial.Serial("com1", 115200, timeout=1)
#     func = cmds.FUNC()
#     data = func.IMPedancequery
#     data = data.encode()
#     ser.write(data)
#     res = ser.readline()
#     try:
#         res = res.decode()
#     except:
#         res = str(res)
#     print(res, end="")

# while True:
#     data = input(">>>")
#     data += "\n"
#     data = data.encode()
#     ser.write(data)
#     res = ser.readline()
#     try:
#         res = res.decode()
#     except:
#         res = str(res)
#     print(res, end="")


if __name__ == "__main__":
    main()
