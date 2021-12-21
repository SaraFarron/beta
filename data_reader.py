from serial import Serial, SerialException
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import random


BAUDRATE = 9600
PORT = 'COM6'
IS_CONNECTED = False
TEST_COUNT = 0


def test_data():
    global TEST_COUNT
    TEST_COUNT += 1

    if TEST_COUNT == 100:
        TEST_COUNT = 0
        return 'X'
    return ' ' + str(random() * 1000) + '\n'


def read_port():

    with Serial() as ser:
        ser.baudrate = BAUDRATE
        ser.port = PORT
        global IS_CONNECTED

        try:
            ser.open()
            content = ser.readline()
            if not IS_CONNECTED:
                print(f"Соединение установлено, baudrate = {BAUDRATE}, порт {PORT}")

        except SerialException:
            if IS_CONNECTED:
                print("Соединение потеряно или порт не был найден")
            IS_CONNECTED = False
            return
        IS_CONNECTED = True

        content = content.decode()
        return content.rstrip()


def parsed_data():
    data = []

    while True:
        raw_data = read_port()
        # raw_data = test_data()

        if not raw_data:
            continue
        elif raw_data == 'X':
            print(f"Прочитан массив: {data[0]}, {data[1]}, {data[2]}...")
            return data
        else:
            try:
                data.append(float(raw_data))
            except ValueError:
                if len(raw_data) > 50:
                    print(f"Ошибка перевода {raw_data[:50]}... в число")
                else:
                    print(f"Ошибка перевода {raw_data} в число")
        

def animate(i):
        data = parsed_data()
        plt.cla()
        plt.grid()
        plt.plot(data)


if __name__ == '__main__':
    print('Ожидание подключения...')
    ani = FuncAnimation(plt.gcf(), animate, interval=10)

    plt.show()
