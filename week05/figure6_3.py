import numpy as np
import matplotlib.pyplot as plt
# from scipy.signal import convolve
from utils import konvolusi_1d

# Approximate input signal (left image): combination of sine + ramp
n_input = 81
n = np.arange(n_input)
sinus = 1 * np.sin(2 * np.pi * n / 20)
ramp = np.linspace(-1.5, 3.5, n_input)
x = sinus + ramp

# Approximate impulse response (middle image): smooth arch, peak ≈ 0.06
# Using windowed shape similar to a parabola or Hanning
n_imp = 31
n = np.arange(n_imp)
center = (n_imp - 1) / 2
h = 1 - ((n - center) / center)**2  # parabola
h = np.clip(h, 0, None)             # make sure values are non-negative

# Normalize to match gain in example (so ramp passes through properly)
h /= np.sum(h)

# Perform convolution
y = konvolusi_1d(x, h)  # output will be len(x) + len(h) - 1 = 111

# Plot
plt.figure(figsize=(15, 4))

# Input
plt.subplot(1, 3, 1)
plt.stem(x, use_line_collection=True)
plt.title("Input Signal")
plt.xlabel("Sample number")
plt.ylim([-2, 4])
plt.grid(True)

# Impulse Response
plt.subplot(1, 3, 2)
plt.stem(h, use_line_collection=True)
plt.title("Impulse Response (Low-pass)")
plt.xlabel("Sample number")
plt.ylim([-0.02, 0.08])
plt.grid(True)

# Output
plt.subplot(1, 3, 3)
plt.plot(y)
plt.title("Output Signal (Low-pass Result)")
plt.xlabel("Sample number")
plt.ylim([-2, 4])
plt.grid(True)

plt.tight_layout()
plt.show()
