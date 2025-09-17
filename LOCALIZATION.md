# PySide6本地化实现说明

## 概述

本文档说明了如何在本项目中实现和使用PySide6的本地化功能。系统支持多语言界面，用户可以在运行时切换界面语言。

## 架构组成

### 1. LanguageManager（语言管理器）
- 位置：[src/ui/language_manager.py](file:///D:/Desktop_Li/code/IQC/src/ui/language_manager.py)
- 功能：管理应用程序的多语言支持
- 特性：
  - 支持的语言列表管理
  - 动态语言切换
  - 翻译文件加载和卸载

### 2. AppState（应用状态管理器）
- 位置：[src/ui/app_state.py](file:///D:/Desktop_Li/code/IQC/src/ui/app_state.py)
- 功能：全局单例，用于在应用各组件间共享LanguageManager实例
- 实现：单例模式，确保全局唯一实例

### 3. LanguageDialog（语言选择对话框）
- 位置：[src/ui/language_dialog.py](file:///D:/Desktop_Li/code/IQC/src/ui/language_dialog.py)
- 功能：提供图形界面供用户选择语言

## 使用方法

### 在代码中添加可翻译文本

在任何继承自QObject的类中，使用以下方法标记可翻译文本：

```python
# 方法1：使用tr()方法（推荐在类内部使用）
self.setWindowTitle(self.tr("窗口标题"))

# 方法2：使用QCoreApplication.translate（推荐在类外部使用）
from PySide6.QtCore import QCoreApplication
text = QCoreApplication.translate("ContextName", "可翻译文本")
```

### 添加新语言支持

1. 在LanguageManager.SUPPORTED_LANGUAGES中添加新语言条目
2. 创建对应的翻译文件目录和文件
3. 使用lupdate工具提取新的翻译条目
4. 使用Qt Linguist完成翻译
5. 使用lrelease编译翻译文件

### 切换语言

```python
# 获取语言管理器
from ui import AppState
app_state = AppState()
language_manager = app_state.get_language_manager()

# 切换到指定语言
language_manager.switch_language('zh_CN')  # 切换到简体中文
language_manager.switch_language('en_US')  # 切换到英文
```

## 翻译文件维护流程

### 1. 提取待翻译文本

使用PySide6提供的lupdate工具从源代码中提取待翻译文本：

```bash
# 在项目根目录下执行以下命令（Windows环境下）
pyside6-lupdate src/ui/app_state.py src/ui/cmdWin.py src/ui/comDlg.py src/ui/language_dialog.py src/ui/language_manager.py src/ui/mainWin.py src/ui/setsDlg.py src/ui/startDlg.py src/ui/Win2837.py src/ui/Win5235.py .\src\template\com.ui .\src\template\commandWin.ui .\src\template\MainWin.ui .\src\template\start.ui -ts translations/zh/app_zh.ts

pyside6-lupdate src/ui/app_state.py src/ui/cmdWin.py src/ui/comDlg.py src/ui/language_dialog.py src/ui/language_manager.py src/ui/mainWin.py src/ui/setsDlg.py src/ui/startDlg.py src/ui/Win2837.py src/ui/Win5235.py .\src\template\com.ui .\src\template\commandWin.ui .\src\template\MainWin.ui .\src\template\start.ui -ts .\translations\en\app_en.ts
```

注意：由于Windows环境下通配符支持可能存在问题，建议明确列出所有需要处理的Python文件。

对于使用Qt Designer创建的.ui文件，它们在通过pyside6-uic转换为Python代码后，其中的`QCoreApplication.translate()`调用也会被lupdate正确识别。

### 2. 编辑翻译文件

使用Qt Linguist工具打开.ts文件进行翻译。

### 3. 编译翻译文件

使用lrelease工具将.ts文件编译为.qm二进制文件：

```bash
# 在项目根目录下执行以下命令
pyside6-lrelease translations/zh/app_zh.ts
pyside6-lrelease translations/en/app_en.ts
```

## 最佳实践

1. 在所有用户可见的文本上使用tr()或QCoreApplication.translate()
2. 为每个窗口或对话框使用唯一的context名称
3. 定期更新翻译文件以包含最新的界面文本
4. 在添加新功能时及时更新翻译文件
5. 保持翻译文本与源语言文本的一致性
6. 确保所有包含翻译调用的Python文件都被包含在lupdate命令中

## 常见问题

### 1. 语言切换后界面未更新
确保在切换语言后重新设置相关控件的文本：

```python
# 切换语言后需要手动更新已显示的文本
self.label.setText(self.tr("新文本"))
self.setWindowTitle(self.tr("新窗口标题"))
```

### 2. 新添加的文本未出现在翻译文件中
确保使用了tr()或QCoreApplication.translate()标记文本，然后重新运行lupdate工具。同时确保所有相关文件都被包含在lupdate命令中。

### 3. 翻译文件编译失败
检查.ts文件格式是否正确，确保所有<message>标签都正确闭合。

### 4. lupdate命令执行失败
确保：
- 在项目根目录执行命令
- 使用正确的pyside6-lupdate命令（而不是lupdate）
- 文件路径正确无误
- 在Windows环境下，通配符可能不被支持，建议明确列出所有文件
- 已安装PySide6开发工具

### 5. UI文件中的翻译文本未被识别
使用Qt Designer创建的.ui文件在通过pyside6-uic转换为Python代码后，其中的翻译调用应该能被lupdate正确识别。确保转换后的Python文件被包含在lupdate命令中。