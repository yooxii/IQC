from template.ui_start import *
from . import Win2837
from . import Win5235
from PySide6.QtWidgets import QMenu, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction


class startDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(startDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.tr("开始"))
        
        # 添加语言选择按钮
        self.lang_button = QPushButton(self.tr("语言/Language"))
        self.lang_button.setMenu(self.create_language_menu())
        
        # 将语言按钮添加到布局中
        self.gridLayout_2.addWidget(self.lang_button, 6, 0, 1, 2)
        
        self.btn5235.clicked.connect(self.btn5235_clicked)
        self.btn2837.clicked.connect(self.btn2837_clicked)

    def create_language_menu(self):
        """
        创建语言选择菜单
        
        Returns:
            QMenu: 语言选择菜单
        """
        menu = QMenu(self)
        
        # 添加语言选项
        chinese_action = QAction("简体中文", self)
        english_action = QAction("English", self)
        
        chinese_action.triggered.connect(lambda: self.switch_language("zh_CN"))
        english_action.triggered.connect(lambda: self.switch_language("en_US"))
        
        menu.addAction(chinese_action)
        menu.addAction(english_action)
        
        return menu
    
    def switch_language(self, language_code):
        """
        切换语言
        
        Args:
            language_code (str): 目标语言代码
        """
        # 获取应用程序状态中的语言管理器
        from .app_state import AppState
        app_state = AppState.getInstance()
        language_manager = app_state.get_language_manager()
        
        if language_manager:
            language_manager.switch_language(language_code)
            
            # 重新翻译当前窗口
            self.setWindowTitle(self.tr("开始"))

    def btn2837_clicked(self):
        self.win = Win2837.MainWin()
        self.win.show()
        self.close()

    def btn5235_clicked(self):
        self.win = Win5235.MainWin()
        self.win.show()
        self.close()