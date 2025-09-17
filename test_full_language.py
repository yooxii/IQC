#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
完整测试语言切换功能
测试从AppState到LanguageManager的整个流程
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from PySide6.QtWidgets import QApplication
from src.ui.app_state import AppState
from src.ui.language_manager import LanguageManager


def test_full_language_switch():
    """测试完整语言切换流程"""
    print("测试完整语言切换流程...")
    
    # 创建QApplication实例（Qt翻译功能需要）
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # 创建语言管理器
    language_manager = LanguageManager()
    print(f"支持的语言: {language_manager.get_supported_languages()}")
    
    # 创建AppState并设置语言管理器
    app_state = AppState.getInstance()
    app_state.set_language_manager(language_manager)
    
    # 验证AppState是单例
    app_state2 = AppState.getInstance()
    print(f"AppState单例验证: {app_state is app_state2}")
    
    # 验证语言管理器正确设置
    retrieved_manager = app_state.get_language_manager()
    print(f"语言管理器设置验证: {language_manager is retrieved_manager}")
    
    # 测试语言切换
    print("\n测试语言切换:")
    
    # 切换到中文
    result = language_manager.switch_language("zh_CN")
    current_lang = language_manager.get_current_language()
    print(f"切换到中文 - 结果: {result}, 当前语言: {current_lang}")
    
    # 切换到英文
    result = language_manager.switch_language("en_US")
    current_lang = language_manager.get_current_language()
    print(f"切换到英文 - 结果: {result}, 当前语言: {current_lang}")
    
    print("\n测试完成!")


if __name__ == "__main__":
    test_full_language_switch()