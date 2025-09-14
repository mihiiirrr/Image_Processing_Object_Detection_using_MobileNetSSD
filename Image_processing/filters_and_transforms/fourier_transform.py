import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image (in grayscale)
image = cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Compute the 2D Fourier Transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)  # Shift the zero frequency component to the center
magnitude_spectrum = 20 * np.log(np.abs(f_transform_shifted))  # Magnitude spectrum in dB

# Apply inverse Fourier transform to reconstruct the image
f_transform_inv_shifted = np.fft.ifftshift(f_transform_shifted)
image_reconstructed = np.fft.ifft2(f_transform_inv_shifted)
image_reconstructed = np.abs(image_reconstructed)  # Take the absolute value

# Display the original image, magnitude spectrum, and reconstructed image
plt.figure(figsize=(18, 6))

plt.subplot(131), plt.imshow(image, cmap='gray')
plt.title('Input Image'), plt.axis('off')

plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.axis('off')

plt.subplot(133), plt.imshow(image_reconstructed, cmap='gray')
plt.title('Reconstructed Image'), plt.axis('off')

plt.tight_layout()
plt.show()
