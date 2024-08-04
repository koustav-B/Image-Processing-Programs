from PIL import Image
import matplotlib.pyplot as plt

image_path = "flower.jpg"
# Function to perform and display transformations
def transform_image(image_path):
    # Open an image file
    img = Image.open(image_path)

    # Perform transformations
    rotated = img.rotate(45, expand=True)
    scaled = img.resize((int(img.width * 1.5), int(img.height * 1.5)))
    translated = Image.new('RGB', (img.width + 50, img.height + 50), (255, 255, 255))
    translated.paste(img, (50, 50))

    # Display the original and transformed images
    titles = ['Original', 'Rotated', 'Scaled', 'Translated']
    images = [img, rotated, scaled, translated]

    plt.figure(figsize=(20, 5))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(1, 4, i + 1)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Define the path to the image file

transform_image(image_path)
