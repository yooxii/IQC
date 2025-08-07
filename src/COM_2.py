import serial
import random

ser = serial.Serial("COM2", 115200, timeout=1)

trig_sour = "BUS"

while True:
    data = ""
    dec = ""
    while dec == "":
        dec = ser.readline().decode().strip()
    if dec == "quit":
        break
    if dec != "":
        print(f"dec:{dec}")
    if dec == "DISP:PAGE?":
        send = "< TRANS JUDGE DISP >\n"
    elif dec == "FETC?":
        if trig_sour == "BUS":
            send = f"4: {random.uniform(1,9):.6}e-04, {random.uniform(1,3):.6}e+01, 3\n"
        elif trig_sour == "INT":
            send = f"6: {random.uniform(1,9):.6}e-01, 3\n"
    elif dec == "TRIG":
        send = f"1: {random.uniform(1,9):.6}e-02,+, 3\n"
    elif dec == "TRIG:SOUR INT":
        trig_sour = "INT"
        send = "\n"
    elif dec == "TRIG:SOUR BUS":
        trig_sour = "BUS"
        send = "\n"
    else:
        send = "\n"
        # continue
    print(f"send:{send}", end="")
    ser.write(send.encode())

ser.close()
