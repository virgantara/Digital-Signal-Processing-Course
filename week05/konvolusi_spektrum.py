import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from numpy.fft import fft, ifft, fftshift

# Buat sinyal input (sinyal sinus)
t = np.linspace(0, 1, 256, endpoint=False)
x = np.sin(2 * np.pi * 5 * t)  # 5 Hz sinusoidal signal

# Buat impulse response (misalnya: low-pass FIR filter)
h = np.ones(16) / 16  # Moving average filter (smoothing)

# Konvolusi di domain waktu
y_time = convolve(x, h, mode='same')

# FFT dari masing-masing komponen
X_f = fft(x)
H_f = fft(h, n=len(x))  # padding to same length
Y_f = fft(y_time)

# Perkalian di domain frekuensi
Y_freq = X_f * H_f
y_ifft = np.real(ifft(Y_freq))

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x)
plt.title("Input Signal (Time Domain)")

plt.subplot(3, 2, 2)
plt.plot(np.abs(fftshift(X_f)))
plt.title("Input Spectrum")

plt.subplot(3, 2, 3)
plt.plot(h)
plt.title("Impulse Response")

plt.subplot(3, 2, 4)
plt.plot(np.abs(fftshift(H_f)))
plt.title("Filter Spectrum")

plt.subplot(3, 2, 5)
plt.plot(y_time, label='Time-domain Conv')
plt.plot(y_ifft, '--', label='Freq-domain Mult')
plt.title("Output Signal")
plt.legend()

plt.subplot(3, 2, 6)
plt.plot(np.abs(fftshift(Y_f)))
plt.title("Output Spectrum")

plt.tight_layout()
plt.show()
