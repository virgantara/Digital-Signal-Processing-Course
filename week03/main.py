import numpy as np
import librosa
import matplotlib.pyplot as plt
from util import plot_signal

duration = 0.1        # in seconds
sr = 22000            # sample rate (Hz)
freq = 220              # frequency  (Hz)
t = np.linspace(0, duration, int(sr * duration), endpoint=False)

cosine_signal = np.cos(2 * np.pi * freq * t)
sine_signal = np.sin(2 * np.pi * freq * t)

plot_signal(cosine_signal)
plot_signal(sine_signal)

sine_wave = np.sin(2 * np.pi * freq * t)
cosine_wave = np.cos(2 * np.pi * freq * t)

mixed_signal = 0.5 * sine_wave + 0.5 * cosine_wave
rectified_signal = np.abs(mixed_signal)

plot_signal(rectified_signal)

sr = 1000          # sample rate (Hz)
duration = 1.0     # seconds
freq = 5           # base frequency (Hz)
t = np.linspace(0, duration, int(sr * duration), endpoint=False)

# Build a sharp waveform by adding harmonics
# Fundamental + 2nd + 3rd harmonic
wave = (
    1.0 * np.sin(2 * np.pi * freq * t) +
    0.5 * np.sin(2 * np.pi * 2 * freq * t) +
    0.33 * np.sin(2 * np.pi * 3 * freq * t)
)

# Normalize (optional)
wave /= np.max(np.abs(wave))
plot_signal(wave)