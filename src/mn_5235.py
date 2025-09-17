import serial
import random

ser = serial.Serial("COM2", 38400, timeout=1)


def send_data():
    """
    生成符合TH5235设备格式的测试数据
    每行32字节测试数据，共10项测试，最后加结束符0xa，总长度321字节

    格式说明:
    @- 共1字節, 固定為@, 代表每筆資料的開頭
    A- 共10字節, 繞組編號及點位
    B- 共5字節, 測試項目
    C- 共7字節, 數值
    D- 共2字節, 單位
    E- 共1字節, 空格
    F- 共1字節, + 或 - 表示圈比的極性, 其他測項為空格
    G- 共2字節, 空格
    H- 共2字節, 判定結果, OK, NG, HI或LO
    I- 共1字節, 空格
    """
    # 测试项目列表
    test_items = ["Ls", "Lk", "Q", "ACR", "TR", "O/S", "C", "Ns", "Rp", "Rdc"]

    # 绕组编号及点位格式示例
    winding_info_list = [
        "N1(1,2)",
        "N2(3,4)",
        "N1:N2",
        "PIN(1,2)",
        "N1-N2",
        "N3(5,6)",
        "N2:N3",
        "PIN(3,4)",
        "N1-N3",
        "N4(7,8)",
    ]

    # 单位列表
    units = ["mH", "uH", "nH", "pF", "uF", "nF", "mR", "Oh", "kR"]

    # 判定结果
    results = ["OK", "NG", "HI", "LO"]

    # 构建测试数据
    test_data = ""

    for i in range(10):
        # @符号 (1字节)
        line = "@"

        # 绕组编号及点位 (10字节) - 左对齐
        winding_info = (winding_info_list[i] + " " * 10)[:10]
        line += winding_info

        # 测试项目 (5字节) - 左对齐
        test_item = (test_items[i] + " " * 5)[:5]
        line += test_item

        # 数值 (7字节) - 右对齐
        value = "{:>7.3f}".format(random.uniform(0, 999.999))[:7]
        line += value

        # 单位 (2字节)
        unit = random.choice(units)
        unit = (unit + " " * 2)[:2]
        line += unit

        # 空格 (1字节)
        line += " "

        # 极性 (+/- 或空格) (1字节)
        if test_items[i] == "TR":  # 圈比测试有极性
            polarity = random.choice(["+", "-"])
        else:
            polarity = " "
        line += polarity

        # 空格 (2字节)
        line += "  "

        # 判定结果 (2字节)
        result = random.choice(results)
        line += result

        # 空格 (1字节)
        line += " "

        # 确保每行正好32字节
        line = line[:32]
        test_data += line

    # 添加结束符
    test_data += "\x0a"

    return test_data


while True:
    data = ""
    dec = ""
    while dec == "":
        dec = ser.readline().decode().strip()
    if dec == "quit":
        break
    if dec != "":
        print(f"dec:{dec}")
    if dec == "TEST":
        send = send_data()
    print(f"send:{send}", end="")
    ser.write(send.encode())

ser.close()
