import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import Qt
from ui import *


def main():
    app = QApplication(sys.argv)
    
    # 创建语言管理器
    language_manager = LanguageManager()
    
    # 设置应用程序全局状态
    app_state = AppState.getInstance()
    app_state.set_language_manager(language_manager)
    
    # 切换到系统语言
    language_manager.switch_to_system_language()
    
    window = startDlg()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()