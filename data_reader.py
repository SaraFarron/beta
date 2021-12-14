from serial import Serial, SerialException
from io import TextIOWrapper, BufferedRWPair


def main():
    while True:
        with Serial() as ser:
            ser.baudrate = 9600
            ser.port = 'COM6'
            try:
                ser.open()
            except SerialException:
                print("Соединение потеряно или порт не был найден")
                return
            data = ser.readline()
            print(data)
            # ser.write(b'hello')

if __name__ == '__main__':
    main()
