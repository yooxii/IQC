# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWineEMkbM.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QWidget)
from . import iqc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(331, 274)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/pics/pic/acbel256.gif", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(256, 256))
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
        self.actioncmdwin = QAction(MainWindow)
        self.actioncmdwin.setObjectName(u"actioncmdwin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textOutput = QTextBrowser(self.centralwidget)
        self.textOutput.setObjectName(u"textOutput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutput.sizePolicy().hasHeightForWidth())
        self.textOutput.setSizePolicy(sizePolicy)
        self.textOutput.setMinimumSize(QSize(0, 140))
        self.textOutput.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.textOutput, 1, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btngetpause = QPushButton(self.centralwidget)
        self.btngetpause.setObjectName(u"btngetpause")

        self.gridLayout.addWidget(self.btngetpause, 0, 1, 1, 1)

        self.btngetdatas = QPushButton(self.centralwidget)
        self.btngetdatas.setObjectName(u"btngetdatas")

        self.gridLayout.addWidget(self.btngetdatas, 0, 0, 1, 1)

        self.btngetstop = QPushButton(self.centralwidget)
        self.btngetstop.setObjectName(u"btngetstop")

        self.gridLayout.addWidget(self.btngetstop, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 331, 21))
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_0 = QMenu(self.menubar)
        self.menu_0.setObjectName(u"menu_0")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.MainstatusBar = QStatusBar(MainWindow)
        self.MainstatusBar.setObjectName(u"MainstatusBar")
        MainWindow.setStatusBar(self.MainstatusBar)

        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_1.addAction(self.actioncom)
        self.menu_1.addAction(self.actiondisconn)
        self.menu_0.addAction(self.actionquit)
        self.menu_3.addAction(self.actioncmdwin)
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
        self.actioncmdwin.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u884c", None))
        self.textOutput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u663e\u793a", None))
#if QT_CONFIG(statustip)
        self.btngetpause.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u6570\u636e\u83b7\u53d6", None))
#endif // QT_CONFIG(statustip)
        self.btngetpause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
#if QT_CONFIG(statustip)
        self.btngetdatas.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4ece\u8bbe\u5907\u4e2d\u83b7\u53d6\u6570\u636e", None))
#endif // QT_CONFIG(statustip)
        self.btngetdatas.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e", None))
#if QT_CONFIG(statustip)
        self.btngetstop.setStatusTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u6570\u636e\u83b7\u53d6", None))
#endif // QT_CONFIG(statustip)
        self.btngetstop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.menu_0.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

