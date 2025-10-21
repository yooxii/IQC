from template import *

from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QFontDialog, QComboBox
from PySide6.QtCore import QSettings, QLocale
from PySide6.QtGui import QFont


class setsDialog(QDialog, Ui_MoreSetsDialog):
    def __init__(self, settings: QSettings):
        super().__init__()
        self.setupUi(self)

        self.settings = settings
        self.currentFont = None

        # 添加语言选择框
        self.comb_language = QComboBox(self)
        self.comb_language.addItem("简体中文", "zh_CN")
        self.comb_language.addItem("English", "en_US")
        self.treeWidget.setItemWidget(
            self.treeWidget.topLevelItem(0), 0, self.comb_language
        )

        self.treeWidget.itemClicked.connect(self.setPageChange)
        self.tbtn_fontfamily.clicked.connect(self.getfont)

        self.setShow()

    def setShow(self):
        self.settings.beginGroup("MainWindow")
        fontfamily = self.settings.value("font_family", "Microsoft YaHei UI", type=str)
        fontsize = self.settings.value("font_size", 14, type=int)
        self.currentFont = QFont(fontfamily, pointSize=fontsize)
        self.edit_fontfamily.setText(fontfamily)
        self.spin_fontsize.setValue(fontsize)
        theme = self.settings.value("theme", 0, type=int)
        self.comb_theme.setCurrentIndex(theme)
        atw = self.settings.value("always_top_window", False, type=bool)
        self.check_topwin.setChecked(atw)

        # 读取语言设置
        lang = self.settings.value("language", QLocale.system().name(), type=str)
        lang_index = self.comb_language.findData(lang)
        if lang_index >= 0:
            self.comb_language.setCurrentIndex(lang_index)

        self.settings.endGroup()

        self.settings.beginGroup("Data")
        poioff = self.settings.value("decimal_point_offset", [0, 0, 0, 0], type=list)
        poi = [int(x) for x in poioff]
        self.spin_ls.setValue(poi[0])
        self.spin_q.setValue(poi[1])
        self.spin_rdc.setValue(poi[2])
        self.spin_ns.setValue(poi[3])
        timeout_retries = self.settings.value("timeout_retries", 10, type=int)
        self.spin_timeoutretry.setValue(timeout_retries)
        comptest = self.settings.value("component_test_times", 5, type=int)
        self.spin_comptest.setValue(comptest)
        self.settings.endGroup()

    def setPageChange(self, item: QTreeWidgetItem, col):
        page = item.text(col)

    def getfont(self):
        ff = self.edit_fontfamily.text()
        fs = self.spin_fontsize.value()
        ok, font = QFontDialog().getFont(QFont(ff, fs), self)
        self.currentFont = font
        if ok:
            self.edit_fontfamily.setText(font.family())
            self.spin_fontsize.setValue(font.pointSize())

    def getPointOffest(self):
        ret = []
        ret.append(self.spin_ls.value())
        ret.append(self.spin_q.value())
        ret.append(self.spin_rdc.value())
        ret.append(self.spin_ns.value())
        return ret

    def saveSettings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("font_family", self.edit_fontfamily.text())
        self.settings.setValue("font_size", self.spin_fontsize.value())
        self.settings.setValue("theme", self.comb_theme.currentText())
        self.settings.setValue("always_top_window", self.check_topwin.isChecked())
        # 保存语言设置
        self.settings.setValue("language", self.comb_language.currentData())
        self.settings.endGroup()

        self.settings.beginGroup("Data")
        self.settings.setValue("decimal_point_offset", self.getPointOffest())
        self.settings.setValue("timeout_retries", self.spin_timeoutretry.value())
        self.settings.setValue("component_test_times", self.spin_comptest.value())
        self.settings.endGroup()

        self.settings.beginGroup("Device")
        self.settings.setValue("DISP", self.comb_disp.currentText())
        self.settings.endGroup()

        self.settings.sync()

    def accept(self):
        self.saveSettings()
        return super().accept()
