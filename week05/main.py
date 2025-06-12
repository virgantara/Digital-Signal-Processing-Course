import numpy as np
import matplotlib.pyplot as plt

# Input signal x[n] (example)
x = np.array([0, 1, 2, 1, 1.4, 0, 0.5, 0, -0.5])
# Impulse response h[n]
h = np.array([1, 0.5, -0.5, 0.2])

# Ukuran output: len(x) + len(h) - 1
y_len = len(x) + len(h) - 1
y = np.zeros(y_len)

# Simulasi konvolusi: input-side algorithm
fig, axes = plt.subplots(len(x), 1, figsize=(10, 2 * len(x)))
fig.suptitle('Visualisasi Setiap Kontribusi x[n]*h[n]', fontsize=14)

for i in range(len(x)):
    # Buat impulse response yang digeser dan diskalakan
    h_shifted_scaled = np.zeros(y_len)
    h_shifted_scaled[i:i+len(h)] = x[i] * h
    y += h_shifted_scaled

    # Visualisasi kontribusi masing-masing komponen
    axes[i].stem(h_shifted_scaled, basefmt=" ", linefmt='gray', markerfmt='D', use_line_collection=True)
    axes[i].set_title(f'Kontribusi dari x[{i}] = {x[i]:.2f}')
    axes[i].set_xlim(0, y_len-1)
    axes[i].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Visualisasi hasil akhir konvolusi
plt.figure(figsize=(10, 4))
plt.stem(y, use_line_collection=True)
plt.title('Output y[n] = x[n] * h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
