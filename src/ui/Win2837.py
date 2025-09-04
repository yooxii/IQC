from .mainWin import *
from th2837 import cmds


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
        import re

        print("run")
        page = None
        self.sercom.write(b"DISP:PAGE TJD\n")
        _ = self.sercom.readline()
        self.sercom.write(b"DISP:PAGE?\n")
        page = self.sercom.readline().decode().strip()
        page = re.sub(r"[a-z]+", "", page)
        print(page, end="")
        if page is None or page == "":
            self.error.emit(self.tr("未连接到设备！"))
            return

        datas = {}
        times = 0
        while len(datas) < 4:
            self.messages.emit(
                self.tr("数据获取重试次数:") + f"{times}/{self.timeout_retries}"
            )
            if self.stop:
                break
            if times >= self.timeout_retries:
                raise TimeoutError(self.tr("Data acquisition timeout!"))
            if times % 3 != 0:
                print("TRIG:SOUR BUS")
                self.sercom.write(b"TRIG:SOUR BUS\n")
                _ = self.sercom.readline()
                # time.sleep(0.1)
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
                print("TRIG")
                self.sercom.write(b"TRIG\n")
                datas |= self.dealData(page)
                if len(datas) >= 4:
                    break
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
            else:
                print("TRIG:SOUR INT")
                self.sercom.write(b"TRIG:SOUR INT\n")
                datas |= self.dealData(page)
                print("FETC?")
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)
                self.sercom.write(b"FETC?\n")
                datas |= self.dealData(page)

            if len(datas) >= 4:
                break
            times += 1
            # self.MainstatusBar.showMessage(
            #     self.tr("数据获取重试次数:") + f"{times}/{self.timeout_retries}"
            # )
        datas_sorted = {}
        datas_sorted["Ls"] = datas["Ls"]
        datas_sorted["Q"] = datas["Q"]
        datas_sorted["Rdc"] = datas["Rdc"]
        datas_sorted["Ns"] = datas["Ns"]

        self.getDatasFinished.emit(datas_sorted)
        self.messages.emit(self.tr("数据获取完成"))

    def dealData(self, page):
        data = self.sercom.readline()
        try:
            data = data.decode().strip()
        except:
            data = str(data)
        if page in ["< LCR MEAS DISP >", "< BIN No. DISP >", "< BIN COUNT DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[0])
            print(dec)
        elif page in ["< LIST SWEEP DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[1])
            print(dec)
        elif page in ["< TRANS MEAS DISP >", "< TRANS JUDGE DISP >"]:
            if data == "" or data is None:
                return {}
            dec = cmds.FETC.decode(data, cmds.FETC_TYPES[2])
            print(dec)
        else:
            raise IndexError(f"{page} " + self.tr("Not the measurement interface!"))
        ret = {}
        if "type" in dec.keys():
            if dec["type"] == "Lx":
                ret["Ls"] = dec["dataA"]
                ret["Q"] = dec["dataB"]
            if dec["type"] == "DCR":
                ret["Rdc"] = dec["dataA"]
            if dec["type"] == "TURN":
                ret["Ns"] = dec["dataA"]
        return ret

    def terminate(self):
        self.stop = True
        return super().terminate()


class MainWin(MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

    def getDatas(self):
        if self.btnGetdatas.text() == self.tr("获取数据"):
            self.btnGetdatas.setText(self.tr("终止获取"))
            self.dataThread = DataThread(self.sercom, self.timeout_retries)
            self.dataThread.getDatasFinished.connect(self.updateDatas)
            self.dataThread.messages.connect(
                lambda msg: self.MainstatusBar.showMessage(msg)
            )
            self.dataThread.error.connect(self.getDatasError)
            self.dataThread.start()
        else:
            if not hasattr(self, "dataThread"):
                return
            self.dataThread.terminate()
            self.dataThread.wait()
            self.btnGetdatas.setText(self.tr("获取数据"))
