# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comIIqSuw.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_comDialog(object):
    def setupUi(self, comDialog):
        if not comDialog.objectName():
            comDialog.setObjectName(u"comDialog")
        comDialog.setWindowModality(Qt.WindowModality.NonModal)
        comDialog.resize(240, 240)
        comDialog.setModal(False)
        self.buttonBox = QDialogButtonBox(comDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 190, 220, 40))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Open)
        self.buttonBox.setCenterButtons(False)
        self.groupBox_0 = QGroupBox(comDialog)
        self.groupBox_0.setObjectName(u"groupBox_0")
        self.groupBox_0.setGeometry(QRect(10, 10, 220, 100))
        self.btncomref = QPushButton(self.groupBox_0)
        self.btncomref.setObjectName(u"btncomref")
        self.btncomref.setGeometry(QRect(170, 20, 40, 25))
        self.listcom = QListWidget(self.groupBox_0)
        self.listcom.setObjectName(u"listcom")
        self.listcom.setGeometry(QRect(10, 20, 150, 70))
        self.groupBox_1 = QGroupBox(comDialog)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(10, 120, 220, 60))
        self.combobaud = QComboBox(self.groupBox_1)
        self.combobaud.addItem("")
        self.combobaud.addItem("")
        self.combobaud.addItem("")
        self.combobaud.addItem("")
        self.combobaud.addItem("")
        self.combobaud.setObjectName(u"combobaud")
        self.combobaud.setGeometry(QRect(10, 20, 200, 25))

        self.retranslateUi(comDialog)
        self.buttonBox.accepted.connect(comDialog.accept)
        self.buttonBox.rejected.connect(comDialog.reject)

        self.combobaud.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(comDialog)
    # setupUi

    def retranslateUi(self, comDialog):
        comDialog.setWindowTitle(QCoreApplication.translate("comDialog", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.groupBox_0.setTitle(QCoreApplication.translate("comDialog", u"\u9009\u62e9\u4e32\u53e3", None))
        self.btncomref.setText(QCoreApplication.translate("comDialog", u"\u5237\u65b0", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("comDialog", u"\u6ce2\u7279\u7387", None))
        self.combobaud.setItemText(0, QCoreApplication.translate("comDialog", u"9600", None))
        self.combobaud.setItemText(1, QCoreApplication.translate("comDialog", u"19200", None))
        self.combobaud.setItemText(2, QCoreApplication.translate("comDialog", u"38400", None))
        self.combobaud.setItemText(3, QCoreApplication.translate("comDialog", u"57600", None))
        self.combobaud.setItemText(4, QCoreApplication.translate("comDialog", u"115200", None))

    # retranslateUi

