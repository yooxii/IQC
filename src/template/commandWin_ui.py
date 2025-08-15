# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commandWin.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_commandWindow(object):
    def setupUi(self, commandWindow):
        if not commandWindow.objectName():
            commandWindow.setObjectName(u"commandWindow")
        commandWindow.resize(560, 320)
        self.centralwidget = QWidget(commandWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMaximumSize(QSize(150, 16777215))
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.treeWidget.setIndentation(10)
        self.treeWidget.header().setVisible(False)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_send = QLineEdit(self.centralwidget)
        self.edit_send.setObjectName(u"edit_send")

        self.horizontalLayout.addWidget(self.edit_send)

        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout.addWidget(self.btn_send)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)

        commandWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(commandWindow)
        self.statusBar.setObjectName(u"statusBar")
        commandWindow.setStatusBar(self.statusBar)

        self.retranslateUi(commandWindow)

        QMetaObject.connectSlotsByName(commandWindow)
    # setupUi

    def retranslateUi(self, commandWindow):
        commandWindow.setWindowTitle(QCoreApplication.translate("commandWindow", u"CMD", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("commandWindow", u"\u547d\u4ee4", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("commandWindow", u"\u8fd4\u56de\u6d4b\u91cf\u6570\u636e", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("commandWindow", u"\u89e6\u53d1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("commandWindow", u"\u89e6\u53d1\u4e00\u6b21", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("commandWindow", u"\u89e6\u53d1\u6e90", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("commandWindow", u"\u81ea\u52a8", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("commandWindow", u"\u624b\u52a8", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem4.child(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("commandWindow", u"\u603b\u7ebf", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem4.child(3)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("commandWindow", u"\u5916\u90e8", None));
        ___qtreewidgetitem9 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("commandWindow", u"\u4eea\u5668\u9875\u9762", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("commandWindow", u"\u5143\u4ef6\u6d4b\u91cf\u663e\u793a", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("commandWindow", u"\u6863\u53f7\u663e\u793a", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem9.child(2)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("commandWindow", u"\u6863\u8ba1\u6570\u663e\u793a", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem9.child(3)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("commandWindow", u"\u5217\u8868\u626b\u63cf\u663e\u793a", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem9.child(4)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("commandWindow", u"\u6d4b\u91cf\u8bbe\u7f6e", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem9.child(5)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("commandWindow", u"\u7528\u6237\u6821\u6b63\u529f\u80fd", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem9.child(6)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("commandWindow", u"\u6781\u9650\u5217\u8868\u8bbe\u7f6e", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem9.child(7)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("commandWindow", u"\u5217\u8868\u626b\u63cf\u8bbe\u7f6e", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem9.child(8)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("commandWindow", u"\u7cfb\u7edf\u8bbe\u7f6e\u9875\u9762", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem9.child(9)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("commandWindow", u"\u53d8\u538b\u5668\u6d4b\u8bd5\u8bbe\u7f6e", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem9.child(10)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("commandWindow", u"\u53d8\u538b\u5668\u6781\u9650\u8bbe\u7f6e", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem9.child(11)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("commandWindow", u"\u53d8\u538b\u5668\u6d4b\u91cf\u663e\u793a", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem9.child(12)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("commandWindow", u"\u53d8\u538b\u5668\u5224\u522b\u663e\u793a", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem9.child(13)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("commandWindow", u"\u53d8\u538b\u5668\u626b\u63cf\u6d4b\u8bd5\u9875\u9762", None));
        ___qtreewidgetitem24 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("commandWindow", u"\u6d4b\u91cf\u901f\u5ea6", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("commandWindow", u"\u6162", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem24.child(1)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("commandWindow", u"\u4e2d", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem24.child(2)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("commandWindow", u"\u5feb", None));
        ___qtreewidgetitem28 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("commandWindow", u"\u67e5\u8be2", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("commandWindow", u"\u5f53\u524d\u9875\u9762", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem28.child(1)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("commandWindow", u"\u89e6\u53d1\u6e90", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem28.child(2)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("commandWindow", u"\u6d4b\u91cf\u901f\u5ea6", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.btn_send.setText(QCoreApplication.translate("commandWindow", u"\u53d1\u9001", None))
    # retranslateUi

