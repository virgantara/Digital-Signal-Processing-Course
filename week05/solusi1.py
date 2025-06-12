import numpy as np
import matplotlib.pyplot as plt

# Sinyal dan kernel
x = np.array([0, 2, 3, 2, 0])
h = np.array([1, 0, -1])

# Konvolusi manual (mode='full' untuk ilustrasi lengkap)
y = np.convolve(x, h, mode='full')

# Visualisasi
plt.figure(figsize=(10, 4))
plt.stem(range(len(x)), x, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title('Input Signal x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.stem(range(len(h)), h, linefmt='g-', markerfmt='go', basefmt=' ')
plt.title('Kernel h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.stem(range(len(y)), y, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.title('Output Signal y[n] = x[n] * h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
