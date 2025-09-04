def decode(data):
    """解析测试结果数据

    Args:
        data (str): 测试结果数据

    Returns:
        list: 解析后的测试结果数据
    """

    if isinstance(data, bytes):
        data = data.decode()
    length = len(data)
    # 找到@的位置，为开头
    start = data.find("@")

    # 按照格式要求解析数据
    test_results = []

    # 从找到的第一个@开始处理数据
    while start < length and start != -1:
        # 每行数据长度为32字节，加上结束符共33字节
        if start + 32 <= length:
            line = data[start : start + 33]  # 包含可能的结束符
            if line.endswith("\n") or line.endswith("\x0a"):
                line = line.rstrip("\n\x0a")

            # 解析每行测试数据，按照指定格式分割
            if len(line) >= 32 and line[0] == "@":
                parsed_data = {
                    "winding_info": line[1:11],  # 绕组编号及点位(10字节)
                    "test_item": line[11:16],  # 测试项目(5字节)
                    "value": line[16:23],  # 数值(7字节)
                    "unit": line[23:25],  # 单位(2字节)
                    "polarity": line[26],  # 极性(+/-)(1字节)
                    "result": line[29:31],  # 判定结果(2字节)
                }
                test_results.append(parsed_data)

            # 查找下一个@位置
            next_start = data.find("@", start + 1)
            # 如果没有找到下一个@，或者到达结束符，则停止
            if next_start == -1 or "\x0a" in data[start:]:
                break
            start = next_start
        else:
            break

    return test_results
