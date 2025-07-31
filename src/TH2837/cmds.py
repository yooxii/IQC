"""命令的封装"""

import re


STATE = ["ON", "OFF", "1", "0"]
FETC_TYPES = ["component", "list", "transformer"]


def find_unit(value: str, units):
    res = []
    for ut in units:
        if ut in value:
            res.append(ut)
    return max(res, key=len) if res else ""


class DISP:
    """用于设定仪器的显示页面和查询当前页面"""

    page = [
        "MEAS",
        "BNUM",
        "BCO",
        "LIST",
        "MSET",
        "CSET",
        "LTAB",
        "LSET",
        "SYST",
        "FLIS",
        "TTS",
        "TLS",
        "TMD",
        "TJD",
        "TSD",
    ]

    font = ["LARG", "TINY", "OFF"]

    @classmethod
    def PAGEquery(self):
        return f"DISP:PAGE?\n".encode()

    @classmethod
    def LINEquery(self):
        return f"DISP:LINE?\n".encode()

    @classmethod
    def RFONtquery(self):
        return f"DISP:RFON?\n".encode()

    @classmethod
    def PAGE(self, page="MEAS"):
        if page not in self.page:
            raise ValueError("Invalid page")
        return f"DISP:PAGE {page}\n".encode()

    @classmethod
    def LINE(self, line: str):
        return f'DISP:LINE "{line}"\n'.encode()

    @classmethod
    def RFONt(self, font="LARG"):
        if font not in self.font:
            raise ValueError("Invalid font")
        return f"DISP:RFON {font}\n".encode()


class RANG:
    """过渡类"""

    unit = ["OHM", "KOHM"]
    cmd = "RANG"

    def __init__(self, _unit=None, _cmd=None, MINMAX=True):
        if _unit:
            self.unit = _unit
        if _cmd:
            self.cmd = _cmd
        self.MINMAX = MINMAX

    def set(self, value: str):
        value = value.upper()
        if self.MINMAX:
            if value == "MIN":
                return self.setMIN
            if value == "MAX":
                return self.setMAX
        else:
            if "MIN" in value or "MAX" in value:
                raise ValueError(f"Invalid {self.cmd} value: {value}")
        unit = find_unit(value, self.unit)
        num = re.sub(unit, "", value)
        if not num or not unit:
            raise ValueError(f"Invalid {self.cmd} value: {value}")
        try:
            num = int(num)
        except ValueError:
            raise ValueError(f"Invalid {self.cmd} value: {value}")
        if unit not in self.unit:
            raise ValueError(f"Invalid {self.cmd} unit: {unit}")
        return f"{self.cmd} {value}\n"

    @classmethod
    def query(self):
        return f"{self.cmd}?\n"

    @classmethod
    def setMIN(self):
        return f"{self.cmd} MIN\n"

    @classmethod
    def setMAX(self):
        return f"{self.cmd} MAX\n"


class FREQ(RANG):
    """用于设定仪器的频率范围和查询当前频率"""

    def __init__(self):
        self.unit = ["HZ", "KHZ", "MHZ"]
        self.cmd = "FREQ"


class VOLT(RANG):
    """用于设定和查询仪器当前的测量电平电压"""

    def __init__(self):
        self.cmd = "VOLT"
        self.unit = ["V"]


class CURR(RANG):
    """用于设定和查询仪器当前的测量电平电流"""

    def __init__(self):
        self.cmd = "CURR"
        self.unit = ["MA", "UA"]


class OUTP:
    @classmethod
    def HPOW(self, stat="ON"):
        if stat not in STATE:
            raise ValueError(f"Invalid state: {stat}")
        return f"OUTP:HPOW {stat}\n"

    @classmethod
    def DC_ISOL(self, stat="ON"):
        if stat not in STATE:
            raise ValueError(f"Invalid state: {stat}")
        return f"OUTP:DC:ISOL {stat}\n"

    @classmethod
    def HPOWquery(self):
        return f"OUTP:HPOW?\n"

    @classmethod
    def DC_ISOLquery(self):
        return f"OUTP:DC:ISOL?\n"


class BIAS:
    cmd = "BIAS"

    def __init__(self):
        self.VOLT = VOLT()
        self.CURR = CURR()

    @classmethod
    def STATe(self, stat="ON"):
        if stat not in STATE:
            raise ValueError(f"Invalid state: {stat}")
        return f"BIAS:STAT {stat}\n"

    @classmethod
    def STATequery(self):
        return f"BIAS:STAT?\n"

    def VOLTage(self, value: str):
        return self.VOLT.set(value)

    @classmethod
    def VOLTageMIN(self):
        return f"{self.cmd}:{self.VOLT.setMIN}"

    @classmethod
    def VOLTageMAX(self):
        return f"{self.cmd}:{self.VOLT.setMAX}"

    @classmethod
    def VOLTagequery(self):
        return f"{self.cmd}:{self.VOLT.query}"

    def CURRent(self, value: str):
        return self.CURR.set(value)

    @classmethod
    def CURRentMIN(self):
        return f"{self.cmd}:{self.CURR.setMIN}"

    @classmethod
    def CURRentMAX(self):
        return f"{self.cmd}:{self.CURR.setMAX}"

    @classmethod
    def CURRentquery(self):
        return f"{self.cmd}:{self.CURR.query}"


class FUNC:
    """主要用于设定测量功能，量程，电流电压监视开关，和偏差显示的模式选择、标称设定"""

    cmd = "FUNC"
    rang = RANG(MINMAX=False)
    imp = [
        "CPD",
        "CPQ",
        "CPG",
        "CPRP",
        "CSD",
        "CSQ",
        "CSRS",
        "LPQ",
        "LPD",
        "LPG",
        "LPRP",
        "LSD",
        "LSQ",
        "LSRS",
        "RX",
        "ZTD",
        "ZTR",
        "GB",
        "YTD",
        "YTR",
        "DCR",
    ]

    def IMPedance(self, func: str):
        if func not in self.imp:
            raise ValueError(f"Invalid impedance: {func}")
        return f"{self.cmd}:IMP {func}\n"

    @classmethod
    def IMPedancequery(self):
        return f"{self.cmd}:IMP?\n"

    def IMPedanceRANGe(self, value):
        return f"{self.cmd}:IMP:{self.rang.set(value)}"

    @classmethod
    def IMPedanceRANGquery(self):
        return f"{self.cmd}:IMP:{self.rang.query}"


class FETC:
    """用于让TH2837X/TH2898KX 输出一个测量结果。"""

    cmd = "FETC"

    @classmethod
    def query(self):
        return f"{self.cmd}?\n"

    @staticmethod
    def decode(result: str, type: str):
        """将FETC命令的返回结果解码为python可读形式
        Args:
            result (str): FETC命令的返回结果
            type (str): 输出结果的类型，可以是：\n
                        "component" - 返回元件测量显示、档号显示、档计数显示的结果，\n
                        "list" - 列表扫描页，\n
                        "transformer" - 变压器单机测量。
        """

        transformer_type = ["TURN", "Zx", "Acr", "Lx", "LK", "DCR"]
        res = {}

        if type not in FETC_TYPES:
            raise ValueError(f"Invalid type: {type}")

        data = result.replace("\n", "").split(",")
        if type == FETC_TYPES[0]:
            res = {
                "dataA": float(data[0]),
                "dataB": float(data[1]),
                "status": int(data[2]),
                "No": int(data[3]),
            }
        elif type == FETC_TYPES[1]:
            res = {
                "dataA": float(data[0]),
                "dataB": float(data[1]),
                "status": int(data[2]),
                "judge": int(data[3]),
            }
        elif type == FETC_TYPES[2]:
            res = {
                "type": (
                    transformer_type[int[data[0] - 1]] if 0 < int(data[0]) <= 6 else ""
                ),
                "dataA": float(data[1]),
                "dataB": float(data[2]),
                "status": int(data[3]),
            }
        return res


def main():
    print(FETC.decode("+1.12340E01,2,3,4\n", "transformer"))


if __name__ == "__main__":
    main()
