import cv2
import matplotlib.pyplot as plt

# Function to extract and display low-level features
image_path = "flower.jpg"
def extract_and_display_features(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully loaded
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # Edge detection using Canny
    edges = cv2.Canny(img, 100, 200)

    # Texture extraction using Laplacian
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    # Edge detection using Sobel
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # Gradient in x direction
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # Gradient in y direction
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)

    # Display the original image and features
    titles = ['Original Image', 'Edges (Canny)', 'Textures (Laplacian)', 'Edges (Sobel)']
    images = [img, edges, laplacian, sobel]

    plt.figure(figsize=(20, 5))
    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Define the path to the image file

extract_and_display_features(image_path)
