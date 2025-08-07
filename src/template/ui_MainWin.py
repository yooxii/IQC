# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinBBBLdd.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from . import iqc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(450, 400)
        MainWindow.setMinimumSize(QSize(450, 300))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/pics/pic/acbel256.gif", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(32, 32))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
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
        self.actionsavedatas = QAction(MainWindow)
        self.actionsavedatas.setObjectName(u"actionsavedatas")
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rBtnLs = QRadioButton(self.groupBox)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rBtnLs)
        self.rBtnLs.setObjectName(u"rBtnLs")
        self.rBtnLs.setMaximumSize(QSize(16777215, 20))
        self.rBtnLs.setChecked(True)

        self.gridLayout_2.addWidget(self.rBtnLs, 0, 0, 1, 1)

        self.rBtnQ = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.rBtnQ)
        self.rBtnQ.setObjectName(u"rBtnQ")
        self.rBtnQ.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.rBtnQ, 0, 1, 1, 1)

        self.rBtnRdc = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.rBtnRdc)
        self.rBtnRdc.setObjectName(u"rBtnRdc")
        self.rBtnRdc.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.rBtnRdc, 0, 2, 1, 1)

        self.rBtnNs = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.rBtnNs)
        self.rBtnNs.setObjectName(u"rBtnNs")
        self.rBtnNs.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.rBtnNs, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cboLs = QComboBox(self.groupBox)
        self.cboLs.addItem("")
        self.cboLs.addItem("")
        self.cboLs.addItem("")
        self.cboLs.setObjectName(u"cboLs")

        self.horizontalLayout_2.addWidget(self.cboLs)

        self.cboQ = QComboBox(self.groupBox)
        self.cboQ.addItem("")
        self.cboQ.setObjectName(u"cboQ")

        self.horizontalLayout_2.addWidget(self.cboQ)

        self.cboRdc = QComboBox(self.groupBox)
        self.cboRdc.addItem("")
        self.cboRdc.addItem("")
        self.cboRdc.setObjectName(u"cboRdc")

        self.horizontalLayout_2.addWidget(self.cboRdc)

        self.cboNs = QComboBox(self.groupBox)
        self.cboNs.addItem("")
        self.cboNs.addItem("")
        self.cboNs.addItem("")
        self.cboNs.setObjectName(u"cboNs")

        self.horizontalLayout_2.addWidget(self.cboNs)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_4.addWidget(self.groupBox, 9, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnGetdatas = QPushButton(self.centralwidget)
        self.btnGetdatas.setObjectName(u"btnGetdatas")
        self.btnGetdatas.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.btnGetdatas, 0, 0, 1, 1)

        self.btnGetstop = QPushButton(self.centralwidget)
        self.btnGetstop.setObjectName(u"btnGetstop")
        self.btnGetstop.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.btnGetstop, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 10, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, -1, 2, -1)
        self.tableOutput = QTableWidget(self.centralwidget)
        if (self.tableOutput.columnCount() < 4):
            self.tableOutput.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableOutput.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableOutput.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableOutput.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableOutput.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableOutput.setObjectName(u"tableOutput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableOutput.sizePolicy().hasHeightForWidth())
        self.tableOutput.setSizePolicy(sizePolicy)
        self.tableOutput.setMinimumSize(QSize(300, 80))
        self.tableOutput.setLineWidth(0)
        self.tableOutput.setAutoScrollMargin(12)
        self.tableOutput.setEditTriggers(QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableOutput.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.tableOutput.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableOutput.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableOutput.setGridStyle(Qt.PenStyle.DotLine)
        self.tableOutput.setRowCount(0)
        self.tableOutput.setColumnCount(4)
        self.tableOutput.horizontalHeader().setVisible(True)
        self.tableOutput.horizontalHeader().setDefaultSectionSize(90)
        self.tableOutput.horizontalHeader().setStretchLastSection(True)
        self.tableOutput.verticalHeader().setVisible(True)
        self.tableOutput.verticalHeader().setCascadingSectionResizes(True)
        self.tableOutput.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableOutput)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 7, 1, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy1)
        self.label_1.setMinimumSize(QSize(0, 10))
        self.label_1.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_1)

        self.label_counttest = QLabel(self.centralwidget)
        self.label_counttest.setObjectName(u"label_counttest")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_counttest.sizePolicy().hasHeightForWidth())
        self.label_counttest.setSizePolicy(sizePolicy2)
        self.label_counttest.setMinimumSize(QSize(40, 10))
        self.label_counttest.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_counttest)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 10))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_countcomponent = QLabel(self.centralwidget)
        self.label_countcomponent.setObjectName(u"label_countcomponent")
        sizePolicy2.setHeightForWidth(self.label_countcomponent.sizePolicy().hasHeightForWidth())
        self.label_countcomponent.setSizePolicy(sizePolicy2)
        self.label_countcomponent.setMinimumSize(QSize(40, 10))
        self.label_countcomponent.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_countcomponent)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 10))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_counttotal = QLabel(self.centralwidget)
        self.label_counttotal.setObjectName(u"label_counttotal")
        sizePolicy1.setHeightForWidth(self.label_counttotal.sizePolicy().hasHeightForWidth())
        self.label_counttotal.setSizePolicy(sizePolicy1)
        self.label_counttotal.setMinimumSize(QSize(40, 10))
        self.label_counttotal.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_counttotal)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 7, 0, 2, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 7, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 21))
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
        QWidget.setTabOrder(self.btnGetdatas, self.btnGetstop)

        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_1.addAction(self.actioncom)
        self.menu_1.addAction(self.actiondisconn)
        self.menu_0.addAction(self.actionsavedatas)
        self.menu_0.addAction(self.actionreset)
        self.menu_0.addSeparator()
        self.menu_0.addAction(self.actionquit)
        self.menu_3.addAction(self.actioncmdwin)
        self.menu_3.addAction(self.actionabout)
        self.menu_2.addAction(self.actionsets_reconn)

        self.retranslateUi(MainWindow)
        self.actionquit.triggered.connect(MainWindow.close)

        self.cboNs.setCurrentIndex(0)


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
        self.actionsavedatas.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.actionreset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u6570\u636e\u7c7b\u578b", None))
#if QT_CONFIG(statustip)
        self.rBtnLs.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7535\u611f\u91cf", None))
#endif // QT_CONFIG(statustip)
        self.rBtnLs.setText(QCoreApplication.translate("MainWindow", u"Ls", None))
#if QT_CONFIG(statustip)
        self.rBtnQ.setStatusTip(QCoreApplication.translate("MainWindow", u"\u54c1\u8d28\u56e0\u7d20", None))
#endif // QT_CONFIG(statustip)
        self.rBtnQ.setText(QCoreApplication.translate("MainWindow", u"Q", None))
#if QT_CONFIG(statustip)
        self.rBtnRdc.setStatusTip(QCoreApplication.translate("MainWindow", u"\u76f4\u6d41\u963b\u6297", None))
#endif // QT_CONFIG(statustip)
        self.rBtnRdc.setText(QCoreApplication.translate("MainWindow", u"Rdc", None))
#if QT_CONFIG(statustip)
        self.rBtnNs.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5708\u6570", None))
#endif // QT_CONFIG(statustip)
        self.rBtnNs.setText(QCoreApplication.translate("MainWindow", u"Ns", None))
        self.cboLs.setItemText(0, QCoreApplication.translate("MainWindow", u"uH", None))
        self.cboLs.setItemText(1, QCoreApplication.translate("MainWindow", u"mH", None))
        self.cboLs.setItemText(2, QCoreApplication.translate("MainWindow", u"H", None))

        self.cboQ.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))

        self.cboRdc.setItemText(0, QCoreApplication.translate("MainWindow", u"m\u03a9", None))
        self.cboRdc.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03a9", None))

        self.cboNs.setItemText(0, QCoreApplication.translate("MainWindow", u"uT", None))
        self.cboNs.setItemText(1, QCoreApplication.translate("MainWindow", u"mT", None))
        self.cboNs.setItemText(2, QCoreApplication.translate("MainWindow", u"T", None))

#if QT_CONFIG(statustip)
        self.btnGetdatas.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4eceTH2837\u4e2d\u83b7\u53d6\u6570\u636e", None))
#endif // QT_CONFIG(statustip)
        self.btnGetdatas.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e", None))
#if QT_CONFIG(statustip)
        self.btnGetstop.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5c06\u6570\u636e\u5f55\u5165\u7cfb\u7edf", None))
#endif // QT_CONFIG(statustip)
        self.btnGetstop.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u6570\u636e", None))
        ___qtablewidgetitem = self.tableOutput.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ls", None));
        ___qtablewidgetitem1 = self.tableOutput.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Q", None));
        ___qtablewidgetitem2 = self.tableOutput.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Rdc", None));
        ___qtablewidgetitem3 = self.tableOutput.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ns", None));
#if QT_CONFIG(statustip)
        self.tableOutput.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u663e\u793a\u533a", None))
#endif // QT_CONFIG(statustip)
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u8ba1\u6570:", None))
#if QT_CONFIG(statustip)
        self.label_counttest.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_counttest.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"1.\u8fbe\u5230\u6307\u5b9a\u6d4b\u8bd5\u6b21\u6570\u65f6\u8ba1\u6570\n"
"2.\u53cc\u51fb\u6b64\u5904\u624b\u52a8\u8ba1\u6570", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u4ee5\u624b\u52a8\u8ba1\u6570", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u96f6\u4ef6\u8ba1\u6570:", None))
#if QT_CONFIG(tooltip)
        self.label_countcomponent.setToolTip(QCoreApplication.translate("MainWindow", u"1.\u8fbe\u5230\u6307\u5b9a\u6d4b\u8bd5\u6b21\u6570\u65f6\u8ba1\u6570\n"
"2.\u53cc\u51fb\u6b64\u5904\u624b\u52a8\u8ba1\u6570", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_countcomponent.setStatusTip(QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u4ee5\u624b\u52a8\u8ba1\u6570", None))
#endif // QT_CONFIG(statustip)
        self.label_countcomponent.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8ba1\u6570:", None))
        self.label_counttotal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.menu_0.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

