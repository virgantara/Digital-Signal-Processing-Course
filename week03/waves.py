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

plt.figure(figsize=(10, 5))
plt.plot(t_cont, signal_values, label='Signal (continuous)', color='blue')
plt.stem(t_wave, wave_values, linefmt='C1-', markerfmt='C1o', basefmt=' ', label='Wave (sampled)', use_line_collection=True)
plt.title("Signal vs Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()