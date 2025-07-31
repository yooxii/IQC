import serial

ser = serial.Serial("COM2", 115200, timeout=1)

while True:
    data = ""
    while data == "":
        data = ser.readline()
    dec = data.decode().strip()
    if dec == "quit":
        break
    if dec != "":
        print(f"dec:{dec}")
    if dec == "DISP:PAGE?":
        send = "LIST\n"
    elif dec == "FETC?":
        send = "+1.12340E01,+2.32340E05,0,-1\n"
    else:
        send = ""
        # continue
    print(f"send:{send}", end="")
    ser.write(send.encode())

ser.close()
