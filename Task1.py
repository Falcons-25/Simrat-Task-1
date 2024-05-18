import serial
import time
import serial.serialutil

with open("Altitude.csv", 'w') as file1:
    try:
        ser = serial.Serial('COM4 ', 9600)
        start = time.perf_counter()
        print("0.0000, 0", file=file1)
        while True:
            data = ser.readline().decode('utf-8', errors='ignore').strip()

            print(f'{(time.perf_counter()-start):.3f}, {data}')
            print(f'{(time.perf_counter()-start):.3f}, {data}', file=file1)
    except KeyboardInterrupt:
        print("User terminated operation.")
        print("User terminated operation.", file=file1)
    except serial.serialutil.SerialException:
        print("Arduino disconnected.")
        print("Arduino disconnected.", file=file1)