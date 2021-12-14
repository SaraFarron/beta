from serial import Serial, SerialException
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import random


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


def test_plot_generation():
    """
    For test purposes only
    """

    def animate(i):
        data = [random() for _ in range(100)]
        plt.cla()
        plt.grid()
        plt.plot(data)

    ani = FuncAnimation(plt.gcf(), animate, interval=10)

    plt.show()

if __name__ == '__main__':
    # test_plot_generation()
    main()
