import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# Load gambar lokal
url = "data/cameraman.png"
img_pil = Image.open(url).convert("L")
img = np.array(img_pil)
img = cv2.resize(img, (256, 256))

# FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Ukuran citra dan titik tengah
rows, cols = img.shape
crow, ccol = rows // 2 , cols // 2

# LOW-PASS filter
r_low = 30
low_pass_mask = np.zeros((rows, cols), np.uint8)
cv2.circle(low_pass_mask, (ccol, crow), r_low, 1, thickness=-1)

# HIGH-PASS filter
high_pass_mask = 1 - low_pass_mask

# BAND-PASS filter: pass between r_in and r_out
r_in, r_out = 20, 60
band_pass_mask = np.zeros((rows, cols), np.uint8)
cv2.circle(band_pass_mask, (ccol, crow), r_out, 1, thickness=-1)
cv2.circle(band_pass_mask, (ccol, crow), r_in, 0, thickness=-1)

# Terapkan masker ke domain frekuensi
f_low = fshift * low_pass_mask
f_high = fshift * high_pass_mask
f_band = fshift * band_pass_mask

# Inverse FFT
img_low = np.abs(np.fft.ifft2(np.fft.ifftshift(f_low)))
img_high = np.abs(np.fft.ifft2(np.fft.ifftshift(f_high)))
img_band = np.abs(np.fft.ifft2(np.fft.ifftshift(f_band)))

# Tampilkan hasil
fig, axs = plt.subplots(1, 4, figsize=(16, 4))
axs[0].imshow(img, cmap='gray')
axs[0].set_title("Original")
axs[1].imshow(img_low, cmap='gray')
axs[1].set_title("Low-pass")
axs[2].imshow(img_high, cmap='gray')
axs[2].set_title("High-pass")
axs[3].imshow(img_band, cmap='gray')
axs[3].set_title("Band-pass")

for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()
