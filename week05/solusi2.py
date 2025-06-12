import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load gambar grayscale dari file atau gunakan default OpenCV (gantilah path jika diperlukan)
image = cv2.imread(cv2.samples.findFile('../week03/data/cameraman.png'), cv2.IMREAD_GRAYSCALE)

# Resize agar lebih ringan
image = cv2.resize(image, (128, 128))

# Kernel Laplacian-like untuk edge detection (bukan blur)
kernel = np.array([
    [ 0, -1,  0],
    [-1,  4, -1],
    [ 0, -1,  0]
], dtype=np.float32)

# kernel2 = np.array([
#     [ 1, 1,  1],
#     [-1,  4, -1],
#     [ 0, -1,  0]
# ], dtype=np.float32)

kernel2 = np.ones((3, 3), dtype=np.float32)

# Apply convolution
convolved = cv2.filter2D(image, ddepth=-1, kernel=kernel)

# Tampilkan hasil
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(convolved, cmap='gray')
plt.title('After Convolution (Edge Enhancement)')
plt.axis('off')

plt.tight_layout()
plt.show()
