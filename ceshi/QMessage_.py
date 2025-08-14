from PySide6.QtWidgets import QApplication, QMessageBox


def main():
    app = QApplication([])
    window = QMessageBox(text="uuuii", detailedText="1231213213213")
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
