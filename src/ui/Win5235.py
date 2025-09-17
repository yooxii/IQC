from .mainWin import *
from th5235 import Protocol


class DataThread(QThread):
    getDatasFinished = Signal(dict)
    messages = Signal(str)
    error = Signal(str)

    def __init__(self, sercom: serial.Serial, timeout_retries: int):
        super().__init__()
        self.sercom = sercom
        self.timeout_retries = timeout_retries
        self.stop = False

    def run(self):
        self.sercom.write(b"TEST\n")
        res = self.sercom.readline()
        print(res)
        dec_datas = Protocol.decode(res)
        if dec_datas == []:
            self.error.emit(self.tr("数据获取失败"))
            return
        datas = {}
        for data in dec_datas:
            data["value"] = float(data["value"])
            if data["polarity"] == "-":
                data["value"] = -data["value"]
            test_item = data["test_item"]
            if test_item in ["Ls", "Q", "Rdc", "Ns"]:
                datas[test_item] = data["value"]

        # 重新排序
        datas_sorted = {}
        datas_sorted["Ls"] = datas["Ls"]
        datas_sorted["Q"] = datas["Q"]
        datas_sorted["Rdc"] = datas["Rdc"]
        datas_sorted["Ns"] = datas["Ns"]

        self.getDatasFinished.emit(datas_sorted)
        self.messages.emit(self.tr("数据获取完成"))

    def terminate(self):
        self.stop = True
        return super().terminate()


class MainWin(MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.comdig.combobaud.setCurrentText("38400")
        self.setWindowTitle("5235")
        self.btnGetdatas.setStatusTip("从5235中获取数据")

        self.sercom = self.comdig.comConnect()

    def getDatas(self):
        if self.btnGetdatas.text() == self.tr("获取数据"):
            self.dataThread = DataThread(self.sercom, self.timeout_retries)
            self.dataThread.getDatasFinished.connect(self.updateDatas)
            self.dataThread.messages.connect(
                lambda msg: self.MainstatusBar.showMessage(msg)
            )
            self.dataThread.error.connect(self.getDatasError)
            self.dataThread.start()
            self.btnGetdatas.setText(self.tr("终止获取"))
        else:
            if not hasattr(self, "dataThread"):
                return
            self.dataThread.terminate()
            self.dataThread.wait()
            self.btnGetdatas.setText(self.tr("获取数据"))
