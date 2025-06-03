import numpy as np

def konvolusi_1d(x, h):
	N = len(x)
	M = len(h)

	y = np.zeros(N + M - 1)

	for n in range(len(y)):
		for k in range(M):
			if 0 <= n - k < N:
				y[n] += x[n - k] * h[k]


	return y