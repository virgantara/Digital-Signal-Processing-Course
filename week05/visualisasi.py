import numpy as np
import matplotlib.pyplot as plt

from utils import konvolusi_1d

def gambar53():
    n = np.arange(0, 80)
    ramp = np.linspace(0, 3, len(n))                  
    sine = np.sin(2 * np.pi * n / 20)                
    input_signal = ramp + sine                      

    lp_impulse_response = np.hanning(31)
    lp_impulse_response /= np.sum(lp_impulse_response)  

    delta = np.zeros_like(lp_impulse_response)
    delta[len(delta)//2] = 1
    hp_impulse_response = delta - lp_impulse_response


    output_lp = konvolusi_1d(input_signal, lp_impulse_response)
    output_hp = konvolusi_1d(input_signal, hp_impulse_response)

    fig, axs = plt.subplots(2, 3, figsize=(15, 8))

    axs[0, 0].plot(n, input_signal, 'k')
    axs[0, 0].set_ylabel("Amplitude", fontsize=16)

    axs[0, 1].plot(lp_impulse_response, 'k')

    axs[0, 2].plot(output_lp, 'k')
    axs[0, 2].set_title('Output Signal (Low-pass)', fontsize=16)

    axs[1, 0].plot(n, input_signal, 'k')
    axs[1, 0].set_ylabel("Amplitude", fontsize=16)

    axs[1, 1].plot(hp_impulse_response, 'k')


    axs[1, 2].plot(output_hp, 'k')
    axs[1, 2].set_title('Output Signal (High-pass)', fontsize=16)

    for ax in axs.flat:
        ax.grid(True)
        ax.set_xlabel("Sample number")

    plt.tight_layout()
    plt.show()

def delta_echo():
    n = np.arange(-2, 7)
    delta_echo = np.zeros_like(n, dtype=float)
    delta_echo[n == 0] = 1      # Impuls utama
    delta_echo[n == 4] = 0.6    # Echo (delay 4 sampel, amplitudo 60%)

    # Visualisasi
    plt.figure(figsize=(6, 3))
    plt.stem(n, delta_echo, basefmt=" ", linefmt='k', markerfmt='ks')
    plt.ylim(-2, 2)
    plt.xlim(-2.5, 6.5)
    plt.xticks(np.arange(-2, 7, 1))
    plt.yticks(np.arange(-2, 3, 1))
    plt.xlabel("Sample number")
    plt.ylabel("Amplitude")
    plt.title("d. Echo: Delta + Shifted & Scaled Echo (0.6)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def gambar7a():
    n = np.arange(-2, 7)
    delta = np.zeros_like(n, dtype=float)
    delta[n == 4] = 1

    # Plot fungsi delta
    plt.figure(figsize=(6, 3))
    plt.stem(n, delta, basefmt=" ", linefmt='k', markerfmt='ks')
    plt.ylim(-2, 2)
    plt.xlim(-2.5, 6.5)
    plt.xticks(np.arange(-2, 7, 1))
    plt.yticks(np.arange(-2, 3, 1))
    plt.xlabel("Jumlah Sampel")
    plt.ylabel("Amplitude")
    plt.title("c. Shift: Fungsi Delta dengan delay 4 sampel")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    delta_echo()