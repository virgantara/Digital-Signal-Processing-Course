import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import konvolusi_1d


def contoh_1d():
	fs = 8000
	t = np.linspace(0, 0.01, int(fs * 0.01), endpoint=False)

	x = np.sin(2 * np.pi * 440 * t)

	h = np.array([1, 0, 0.5])
	y = konvolusi_1d(x, h)

	plt.plot(x, label='x[n]')
	plt.plot(y[:len(x)], label='y[n] = x*h')
	plt.title('Konvolusi 1D')
	plt.legend()
	plt.grid()
	plt.show()


if __name__ == '__main__':
	contoh_1d()