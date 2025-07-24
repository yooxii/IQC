# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWin.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.actiondisconn = QAction(MainWindow)
        self.actiondisconn.setObjectName(u"actiondisconn")
        self.actionquit = QAction(MainWindow)
        self.actionquit.setObjectName(u"actionquit")
        self.actionquit.setCheckable(False)
        self.actionquit.setChecked(False)
        self.actionquit.setVisible(True)
        self.actionquit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionquit.setIconVisibleInMenu(True)
        self.actioncom = QAction(MainWindow)
        self.actioncom.setObjectName(u"actioncom")
        self.actioncom.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionsets_reconn = QAction(MainWindow)
        self.actionsets_reconn.setObjectName(u"actionsets_reconn")
        self.actionsets_reconn.setCheckable(True)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 21))
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_0 = QMenu(self.menubar)
        self.menu_0.setObjectName(u"menu_0")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_1.addAction(self.actioncom)
        self.menu_1.addAction(self.actiondisconn)
        self.menu_0.addAction(self.actionquit)
        self.menu_3.addAction(self.actionabout)
        self.menu_2.addAction(self.actionsets_reconn)

        self.retranslateUi(MainWindow)
        self.actionquit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TH2837", None))
        self.actiondisconn.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u8fde\u63a5", None))
#if QT_CONFIG(statustip)
        self.actiondisconn.setStatusTip(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u4e32\u53e3\u4ee5\u89e3\u9664\u5360\u7528", None))
#endif // QT_CONFIG(statustip)
        self.actionquit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(statustip)
        self.actionquit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionquit.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
#endif // QT_CONFIG(whatsthis)
        self.actioncom.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3...", None))
#if QT_CONFIG(statustip)
        self.actioncom.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5e76\u6253\u5f00\u4e32\u53e3", None))
#endif // QT_CONFIG(statustip)
        self.actionsets_reconn.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u65f6\u6062\u590d\u4e0a\u4e00\u6b21\u8fde\u63a5", None))
#if QT_CONFIG(statustip)
        self.actionsets_reconn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.menu_0.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

