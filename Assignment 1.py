import numpy as np
import matplotlib.pyplot as plt


def sin_cos(x:float):
    """
    :param x: Interval of period
    :return: Sin and cos plot
    """
    sin = np.sin(x)
    cos = np.cos(x)

    # plot 1 period of sin and cos on the same axes
    fig, ax = plt.subplots()
    ax.plot(x, sin, label='sin')
    ax.plot(x, cos, label='cos')
    plt.axhline(y=0, color='k', linestyle='-')
    ax.set_xlim(0, 2*np.pi)
    ax.set_title('One period of sin and cos')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x = np.linspace(0, 2 * np.pi, 1000)
    sin_cos(x)
