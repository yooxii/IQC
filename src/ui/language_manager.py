#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
语言管理器模块
用于处理应用程序的多语言支持和动态切换
"""

import os
from PySide6.QtCore import QTranslator, QLocale, QObject, Signal
from PySide6.QtWidgets import QApplication


class LanguageManager(QObject):
    """语言管理器类"""
    
    # 语言切换信号
    languageChanged = Signal(str)
    
    # 支持的语言列表
    SUPPORTED_LANGUAGES = {
        'zh_CN': '简体中文',
        'en_US': 'English',
    }
    
    def __init__(self, parent=None):
        """
        初始化语言管理器
        
        Args:
            parent: 父对象
        """
        super().__init__(parent)
        self._current_language = None
        self._translators = {}  # 存储已加载的翻译器
        self._app = QApplication.instance()
        
        # 初始化翻译器
        self._init_translators()
    
    def _init_translators(self):
        """
        初始化所有支持语言的翻译器
        """
        # 确定翻译文件路径
        base_path = os.path.join(os.path.dirname(__file__), "..", "..", "translations")
        
        for lang_code in self.SUPPORTED_LANGUAGES.keys():
            translator = QTranslator()
            
            # 根据语言代码确定翻译文件路径
            if lang_code.startswith('zh'):
                qm_file = os.path.join(base_path, "zh", "app_zh.qm")
            else:
                qm_file = os.path.join(base_path, "en", "app_en.qm")
            
            # 如果翻译文件存在，则加载
            if os.path.exists(qm_file):
                if translator.load(qm_file):
                    self._translators[lang_code] = translator
    
    def get_current_language(self):
        """
        获取当前语言
        
        Returns:
            str: 当前语言代码
        """
        return self._current_language
    
    def get_supported_languages(self):
        """
        获取支持的语言列表
        
        Returns:
            dict: 语言代码和显示名称的映射
        """
        return self.SUPPORTED_LANGUAGES
    
    def switch_language(self, language_code):
        """
        切换语言
        
        Args:
            language_code (str): 目标语言代码
        """
        # 移除当前翻译器
        if self._current_language and self._current_language in self._translators:
            self._app.removeTranslator(self._translators[self._current_language])
        
        # 安装新的翻译器
        if language_code in self._translators:
            self._app.installTranslator(self._translators[language_code])
            self._current_language = language_code
            self.languageChanged.emit(language_code)
            return True
        else:
            # 如果没有找到对应语言的翻译器，使用系统默认语言
            self._current_language = QLocale.system().name()
            self.languageChanged.emit(self._current_language)
            return False
    
    def switch_to_system_language(self):
        """
        切换到系统语言
        """
        system_locale = QLocale.system().name()
        # 如果系统语言在支持列表中，使用系统语言，否则默认使用英语
        if system_locale in self.SUPPORTED_LANGUAGES:
            return self.switch_language(system_locale)
        else:
            return self.switch_language('en_US')