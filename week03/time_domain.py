import numpy as np
import librosa
import matplotlib.pyplot as plt

file_path = "data/catsound.wav"
y, sr = librosa.load(file_path, sr=None)
y = y[:sr]

t = np.linspace(0, len(y) / sr, num=len(y))

N = len(y)
fft_vals = np.fft.rfft(y)
frequencies = np.fft.rfftfreq(N, d=1/sr)
magnitude = np.abs(fft_vals)
phase = np.angle(fft_vals)

plt.figure(figsize=(15, 8))

plt.subplot(3, 1, 1)
plt.plot(t, y)
plt.title("Time-Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(frequencies, magnitude)
plt.title("Magnitude Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 8000)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(frequencies, phase)
plt.title("Phase Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.xlim(0, 8000)
plt.grid(True)

plt.tight_layout()
plt.show()
