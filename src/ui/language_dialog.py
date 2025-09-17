#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
语言选择对话框
允许用户在应用程序中切换语言
"""

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLabel
from PySide6.QtCore import Qt, QCoreApplication


class LanguageDialog(QDialog):
    """语言选择对话框类"""
    
    def __init__(self, language_manager, parent=None):
        """
        初始化语言选择对话框
        
        Args:
            language_manager: 语言管理器实例
            parent: 父窗口
        """
        super().__init__(parent)
        self.language_manager = language_manager
        self.setup_ui()
        self.setup_connections()
        self.setWindowTitle(QCoreApplication.translate("LanguageDialog", "语言设置"))
        
    def setup_ui(self):
        """设置界面"""
        layout = QVBoxLayout(self)
        
        # 说明标签
        label = QLabel(QCoreApplication.translate("LanguageDialog", "请选择界面语言:"))
        layout.addWidget(label)
        
        # 语言选择下拉框
        self.language_combo = QComboBox()
        supported_languages = self.language_manager.get_supported_languages()
        for code, name in supported_languages.items():
            self.language_combo.addItem(name, code)
            
        # 设置当前选中语言
        current_lang = self.language_manager.get_current_language()
        if current_lang:
            index = self.language_combo.findData(current_lang)
            if index >= 0:
                self.language_combo.setCurrentIndex(index)
        
        layout.addWidget(self.language_combo)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        
        # 确定按钮
        self.ok_button = QPushButton(QCoreApplication.translate("LanguageDialog", "确定"))
        # 取消按钮
        self.cancel_button = QPushButton(QCoreApplication.translate("LanguageDialog", "取消"))
        
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        # 设置默认按钮
        self.ok_button.setDefault(True)
        self.ok_button.setAutoDefault(True)
        
    def setup_connections(self):
        """连接信号和槽"""
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
    def get_selected_language(self):
        """
        获取选中的语言代码
        
        Returns:
            str: 选中的语言代码
        """
        return self.language_combo.currentData()
        
    def accept(self):
        """确认选择"""
        selected_language = self.get_selected_language()
        if selected_language:
            self.language_manager.switch_language(selected_language)
        super().accept()