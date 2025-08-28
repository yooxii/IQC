from PySide6.QtWidgets import QApplication
from PySide6.QtGui import Qt
from ui import *


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
