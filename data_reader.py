from serial import Serial, SerialException
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import random


BAUDRATE = 9600
PORT = 'COM6'


def animate(i):
        data = [random() for _ in range(100)]
        plt.cla()
        plt.grid()
        plt.plot(data)

while True:
    with Serial() as ser:
        ser.baudrate = BAUDRATE
        ser.port = PORT

        try:
            ser.open()

        except SerialException:
            print("Соединение потеряно или порт не был найден")
            break
        data = ser.readline()
        size = len(data)
        ani = FuncAnimation(plt.gcf(), animate, interval=10)

        plt.show()
