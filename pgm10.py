import cv2
import matplotlib.pyplot as plt

# Function to blur and smooth an image
def blur_and_smooth_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Apply Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Apply Median Blur
    median_blur = cv2.medianBlur(img, 15)

    # Apply Bilateral Filter
    bilateral_filter = cv2.bilateralFilter(img, 15, 75, 75)

    # Display the original and blurred images
    titles = ['Original Image', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
    images = [img, gaussian_blur, median_blur, bilateral_filter]

    plt.figure(figsize=(20, 5))
    for i in range(4):
        plt.subplot(1, 4, i + 1)
        # Convert BGR to RGB for display
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Define the path to the image file
image_path = "Manasa.jpg"
blur_and_smooth_image(image_path)
