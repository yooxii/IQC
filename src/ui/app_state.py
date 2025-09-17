#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
应用程序状态管理器
用于在应用程序中共享全局状态，如语言管理器实例
"""

from PySide6.QtCore import QObject


class AppState(QObject):
    """应用程序状态管理器"""
    
    _instance = None
    _language_manager = None
    
    def __new__(cls, parent=None):
        """
        单例模式实现
        
        Returns:
            AppState: AppState实例
        """
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance
    
    def __init__(self, parent=None):
        """
        初始化AppState
        
        Args:
            parent: 父对象
        """
        if self.__initialized:
            return
        super().__init__(parent)
        self.__initialized = True
    
    @classmethod
    def getInstance(cls):
        """
        获取AppState单例实例
        
        Returns:
            AppState: AppState实例
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def set_language_manager(self, language_manager):
        """
        设置语言管理器实例
        
        Args:
            language_manager: 语言管理器实例
        """
        self._language_manager = language_manager
    
    def get_language_manager(self):
        """
        获取语言管理器实例
        
        Returns:
            LanguageManager: 语言管理器实例
        """
        return self._language_manager