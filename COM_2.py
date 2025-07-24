import serial

ser = serial.Serial("COM2", 115200, timeout=1)

while True:
    data = None
    while data is None:
        data = ser.readline()
    if data.decode() == "quit\n":
        break
    ser.write(data)

ser.close()
