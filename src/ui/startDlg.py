from template.ui_start import *
from . import Win2837
from . import Win5235


class startDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(startDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("开始")
        self.btn5235.clicked.connect(self.btn5235_clicked)
        self.btn2837.clicked.connect(self.btn2837_clicked)

    def btn2837_clicked(self):
        self.win = Win2837.MainWin()
        self.win.show()
        self.close()

    def btn5235_clicked(self):
        self.win = Win5235.MainWin()
        self.win.show()
        self.close()
