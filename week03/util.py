import matplotlib.pyplot as plt
import numpy as np

def plot_signal(signal, sr=1000, samples_to_show=500, 
    title="Signal", xlabel="Time (s)", 
    ylabel="Amplitude"):
   
    t = np.arange(len(signal)) / sr

    plt.figure(figsize=(10, 4))
    plt.plot(t[:samples_to_show], signal[:samples_to_show])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
