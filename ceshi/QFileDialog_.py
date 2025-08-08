from PySide6.QtWidgets import QFileDialog, QApplication, QDialog


class DDialog(QDialog):
    def __init__(self):
        super().__init__()
        file = QFileDialog.getSaveFileName(
            None, "123", filter="*.csv;;*.xlsx"
        )
        print(file)


def main():
    app = QApplication([])
    window = DDialog()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
