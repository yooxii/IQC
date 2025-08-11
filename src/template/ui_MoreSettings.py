# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MoreSettingsGHkdKC.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MoreSetsDialog(object):
    def setupUi(self, MoreSetsDialog):
        if not MoreSetsDialog.objectName():
            MoreSetsDialog.setObjectName(u"MoreSetsDialog")
        MoreSetsDialog.resize(487, 320)
        self.gridLayout = QGridLayout(MoreSetsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(MoreSetsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(MoreSetsDialog)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(150, 16777215))
        self.treeWidget.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.groupBox = QGroupBox(MoreSetsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)


        self.retranslateUi(MoreSetsDialog)
        self.buttonBox.accepted.connect(MoreSetsDialog.accept)
        self.buttonBox.rejected.connect(MoreSetsDialog.reject)

        QMetaObject.connectSlotsByName(MoreSetsDialog)
    # setupUi

    def retranslateUi(self, MoreSetsDialog):
        MoreSetsDialog.setWindowTitle(QCoreApplication.translate("MoreSetsDialog", u"Dialog", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u8bbe\u7f6e", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u7a97\u53e3", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u6570\u636e", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MoreSetsDialog", u"GroupBox", None))
    # retranslateUi

