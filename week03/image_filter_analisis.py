import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
from PIL import Image
import cv2

url = "data/cameraman.png"
img_pil = Image.open(url).convert("L")
img = np.array(img_pil)
img = cv2.resize(img, (256, 256))


# Ukuran citra
rows, cols = img.shape

# FFT dan pemusatan spektrum
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Magnitude dan Phase
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # Hindari log(0)
phase_spectrum = np.angle(fshift)

# Plot hasil
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(img, cmap='gray')
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(magnitude_spectrum, cmap='gray')
axs[1].set_title("Magnitude Spectrum")
axs[1].axis('off')

axs[2].imshow(phase_spectrum, cmap='gray')
axs[2].set_title("Phase Spectrum")
axs[2].axis('off')

plt.tight_layout()
plt.show()
