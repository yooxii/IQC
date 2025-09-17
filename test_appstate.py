#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试AppState单例模式实现
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.app_state import AppState
from src.ui.language_manager import LanguageManager


def test_app_state():
    """测试AppState单例模式"""
    print("测试AppState单例模式...")
    
    # 创建第一个实例
    app_state1 = AppState()
    print(f"AppState 1 ID: {id(app_state1)}")
    
    # 创建第二个实例
    app_state2 = AppState()
    print(f"AppState 2 ID: {id(app_state2)}")
    
    # 通过getInstance方法获取实例
    app_state3 = AppState.getInstance()
    print(f"AppState 3 ID (getInstance): {id(app_state3)}")
    
    # 验证是否为同一实例
    if app_state1 is app_state2 and app_state2 is app_state3:
        print("✓ 单例模式工作正常")
    else:
        print("✗ 单例模式存在问题")
        
    # 测试语言管理器设置和获取
    lang_manager = LanguageManager()
    app_state1.set_language_manager(lang_manager)
    
    retrieved_manager = app_state2.get_language_manager()
    retrieved_manager2 = app_state3.get_language_manager()
    if retrieved_manager is lang_manager and retrieved_manager2 is lang_manager:
        print("✓ 语言管理器共享正常")
    else:
        print("✗ 语言管理器共享存在问题")


if __name__ == "__main__":
    test_app_state()