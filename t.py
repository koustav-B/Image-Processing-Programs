import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = 'flower.jpg'
img = cv2.imread(image_path)

if img is None:
    raise ValueError("Error: Could not load image.")

# Convert the image to RGB (OpenCV uses BGR by default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Grayscale Conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)

# Edge Detection (Canny)
edges = cv2.Canny(gray, 100, 200)

# Sharpening
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

# Thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Histogram Equalization
hist_eq = cv2.equalizeHist(gray)

# Morphological Operations
kernel_morph = np.ones((5, 5), np.uint8)
erosion = cv2.erode(gray, kernel_morph, iterations=1)
dilation = cv2.dilate(gray, kernel_morph, iterations=1)

# Median Blurring
median_blur = cv2.medianBlur(img, 15)

# Color Space Conversion (HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Image Resizing
resized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# Image Rotation
center = (img.shape[1] // 2, img.shape[0] // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

# Image Translation
matrix_translation = np.float32([[1, 0, 50], [0, 1, 50]])  # Translate 50 pixels right and down
translated = cv2.warpAffine(img, matrix_translation, (img.shape[1], img.shape[0]))

# Perspective Transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
matrix_perspective = cv2.getPerspectiveTransform(pts1, pts2)
perspective_transformed = cv2.warpPerspective(img, matrix_perspective, (300, 300))

# Displaying the results using matplotlib
plt.figure(figsize=(12, 12))

plt.subplot(3, 4, 1)
plt.title('Original')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(3, 4, 2)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 3)
plt.title('Gaussian Blur')
plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 4)
plt.title('Edges (Canny)')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 5)
plt.title('Sharpened')
plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 6)
plt.title('Thresholding')
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 7)
plt.title('Histogram Equalization')
plt.imshow(hist_eq, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 8)
plt.title('Erosion')
plt.imshow(erosion, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 9)
plt.title('Dilation')
plt.imshow(dilation, cmap='gray')
plt.axis('off')

plt.subplot(3, 4, 10)
plt.title('Median Blurring')
plt.imshow(cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 11)
plt.title('HSV Color Space')
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 12)
plt.title('Resized')
plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
