import numpy as np
import librosa
import matplotlib.pyplot as plt
from util import plot_signal

duration = 0.1        # in seconds
sr = 22000            # sample rate (Hz)
freq = 220              # frequency  (Hz)
t = np.linspace(0, duration, int(sr * duration), endpoint=False)

cosine_signal = np.cos(2 * np.pi * freq * t)

plot_signal(cosine_signal)
