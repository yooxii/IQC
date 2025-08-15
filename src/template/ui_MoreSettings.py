# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MoreSettingsjOKEAR.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QSpinBox, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MoreSetsDialog(object):
    def setupUi(self, MoreSetsDialog):
        if not MoreSetsDialog.objectName():
            MoreSetsDialog.setObjectName(u"MoreSetsDialog")
        MoreSetsDialog.resize(480, 340)
        self.gridLayout = QGridLayout(MoreSetsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(MoreSetsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(MoreSetsDialog)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(0, 16777215))
        self.treeWidget.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.scrollArea = QScrollArea(MoreSetsDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 435, 291))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.edit_fontfamily = QLineEdit(self.groupBox)
        self.edit_fontfamily.setObjectName(u"edit_fontfamily")

        self.horizontalLayout_2.addWidget(self.edit_fontfamily)

        self.tbtn_fontfamily = QToolButton(self.groupBox)
        self.tbtn_fontfamily.setObjectName(u"tbtn_fontfamily")

        self.horizontalLayout_2.addWidget(self.tbtn_fontfamily)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spin_fontsize = QSpinBox(self.groupBox)
        self.spin_fontsize.setObjectName(u"spin_fontsize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_fontsize.sizePolicy().hasHeightForWidth())
        self.spin_fontsize.setSizePolicy(sizePolicy1)
        self.spin_fontsize.setMaximum(50)
        self.spin_fontsize.setValue(9)

        self.horizontalLayout_2.addWidget(self.spin_fontsize)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comb_theme = QComboBox(self.groupBox)
        self.comb_theme.addItem("")
        self.comb_theme.addItem("")
        self.comb_theme.addItem("")
        self.comb_theme.setObjectName(u"comb_theme")

        self.horizontalLayout_3.addWidget(self.comb_theme)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_topwin = QCheckBox(self.groupBox)
        self.check_topwin.setObjectName(u"check_topwin")

        self.horizontalLayout_4.addWidget(self.check_topwin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)

        self.spin_ls = QSpinBox(self.groupBox_2)
        self.spin_ls.setObjectName(u"spin_ls")
        self.spin_ls.setMinimum(-10)
        self.spin_ls.setMaximum(10)

        self.horizontalLayout_5.addWidget(self.spin_ls)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignRight)

        self.spin_q = QSpinBox(self.groupBox_2)
        self.spin_q.setObjectName(u"spin_q")
        self.spin_q.setMinimum(-10)
        self.spin_q.setMaximum(10)

        self.horizontalLayout_5.addWidget(self.spin_q)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignRight)

        self.spin_rdc = QSpinBox(self.groupBox_2)
        self.spin_rdc.setObjectName(u"spin_rdc")
        self.spin_rdc.setMinimum(-10)
        self.spin_rdc.setMaximum(10)

        self.horizontalLayout_5.addWidget(self.spin_rdc)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignRight)

        self.spin_ns = QSpinBox(self.groupBox_2)
        self.spin_ns.setObjectName(u"spin_ns")
        self.spin_ns.setMinimum(-10)
        self.spin_ns.setMaximum(10)

        self.horizontalLayout_5.addWidget(self.spin_ns)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.spin_timeoutretry = QSpinBox(self.groupBox_2)
        self.spin_timeoutretry.setObjectName(u"spin_timeoutretry")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spin_timeoutretry.sizePolicy().hasHeightForWidth())
        self.spin_timeoutretry.setSizePolicy(sizePolicy3)
        self.spin_timeoutretry.setValue(30)

        self.horizontalLayout_7.addWidget(self.spin_timeoutretry)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.spin_comptest = QSpinBox(self.groupBox_2)
        self.spin_comptest.setObjectName(u"spin_comptest")
        self.spin_comptest.setMinimum(1)
        self.spin_comptest.setValue(5)

        self.horizontalLayout_7.addWidget(self.spin_comptest)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.comb_disp = QComboBox(self.groupBox_3)
        self.comb_disp.addItem("")
        self.comb_disp.setObjectName(u"comb_disp")

        self.horizontalLayout_6.addWidget(self.comb_disp)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)


        self.retranslateUi(MoreSetsDialog)
        self.buttonBox.accepted.connect(MoreSetsDialog.accept)
        self.buttonBox.rejected.connect(MoreSetsDialog.reject)

        QMetaObject.connectSlotsByName(MoreSetsDialog)
    # setupUi

    def retranslateUi(self, MoreSetsDialog):
        MoreSetsDialog.setWindowTitle(QCoreApplication.translate("MoreSetsDialog", u"\u8bbe\u7f6e", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u8bbe\u7f6e", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u7a97\u53e3", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u5b57\u4f53", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u4e3b\u9898", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u7f6e\u9876", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u6570\u636e", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u5c0f\u6570\u70b9\u504f\u79fb", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u4eea\u5668", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MoreSetsDialog", u"\u754c\u9762", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MoreSetsDialog", u"\u7a97\u53e3", None))
        self.label.setText(QCoreApplication.translate("MoreSetsDialog", u"\u5b57\u4f53:", None))
        self.tbtn_fontfamily.setText(QCoreApplication.translate("MoreSetsDialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MoreSetsDialog", u"\u5927\u5c0f:", None))
        self.label_2.setText(QCoreApplication.translate("MoreSetsDialog", u"\u4e3b\u9898:", None))
        self.comb_theme.setItemText(0, QCoreApplication.translate("MoreSetsDialog", u"Light", None))
        self.comb_theme.setItemText(1, QCoreApplication.translate("MoreSetsDialog", u"Dark", None))
        self.comb_theme.setItemText(2, QCoreApplication.translate("MoreSetsDialog", u"Follow the system", None))

        self.check_topwin.setText(QCoreApplication.translate("MoreSetsDialog", u"\u4e3b\u7a97\u53e3\u603b\u662f\u7f6e\u9876", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MoreSetsDialog", u"\u6570\u636e", None))
        self.label_4.setText(QCoreApplication.translate("MoreSetsDialog", u"\u5c0f\u6570\u70b9\u504f\u79fb:", None))
        self.label_5.setText(QCoreApplication.translate("MoreSetsDialog", u"Ls", None))
        self.label_6.setText(QCoreApplication.translate("MoreSetsDialog", u"Q", None))
        self.label_7.setText(QCoreApplication.translate("MoreSetsDialog", u"Rdc", None))
        self.label_8.setText(QCoreApplication.translate("MoreSetsDialog", u"Ns", None))
        self.label_9.setText(QCoreApplication.translate("MoreSetsDialog", u"\u8d85\u65f6\u91cd\u8bd5\u6b21\u6570:", None))
        self.label_11.setText(QCoreApplication.translate("MoreSetsDialog", u"\u96f6\u4ef6\u6d4b\u8bd5\u6b21\u6570:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MoreSetsDialog", u"\u4eea\u5668", None))
        self.label_10.setText(QCoreApplication.translate("MoreSetsDialog", u"\u754c\u9762:", None))
        self.comb_disp.setItemText(0, QCoreApplication.translate("MoreSetsDialog", u"\u53d8\u538b\u5668\u5224\u522b\u663e\u793a", None))

    # retranslateUi

