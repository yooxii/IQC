#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试translate函数是否被正确识别
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# 导入一些包含translate调用的模块
from PySide6.QtCore import QCoreApplication

# 模拟一些translate调用
def test_translations():
    # 这些调用应该能被lupdate识别
    text1 = QCoreApplication.translate("comDialog", "串口设置")
    text2 = QCoreApplication.translate("comDialog", "选择串口")
    text3 = QCoreApplication.translate("comDialog", "刷新")
    
    print(f"Text1: {text1}")
    print(f"Text2: {text2}")
    print(f"Text3: {text3}")

if __name__ == "__main__":
    test_translations()