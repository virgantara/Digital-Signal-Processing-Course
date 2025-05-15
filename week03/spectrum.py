import numpy as np
import matplotlib.pyplot as plt

def signal_function(t, freq=5):
    """Ideal continuous signal: sine wave with frequency `freq` Hz."""
    return np.sin(2 * np.pi * freq * t)

t_cont = np.linspace(0, 1, 1000) 
signal_values = signal_function(t_cont)

sr = 50  
t_wave = np.linspace(0, 1, sr, endpoint=False)
wave_values = signal_function(t_wave)


N = len(wave_values)
fft_vals = np.fft.rfft(wave_values)
frequencies = np.fft.rfftfreq(N, d=1/sr)
magnitude = np.abs(fft_vals)

# 6. Plot Spectrum
plt.figure(figsize=(10, 4))
plt.stem(frequencies, magnitude, basefmt=' ', use_line_collection=True)
plt.title("Spectrum of Sampled Wave")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()