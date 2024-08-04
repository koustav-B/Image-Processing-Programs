import cv2

# Define the path to the image file
image_path = "Koustav.jpg"

# Load the image
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print(f"Error: Could not load image at {image_path}")
else:
    original = img
    h, w, channels = img.shape
    half_width = w // 2
    half_height = h // 2

    # Split the image into four quadrants
    TopLeft_quadrant = img[:half_height, :half_width]
    TopRight_quadrant = img[:half_height, half_width:]
    BottomLeft_quadrant = img[half_height:, :half_width]
    BottomRight_quadrant = img[half_height:, half_width:]

    # Display original and quadrants
    cv2.imshow('originalImage', original)
    cv2.imshow('TopLeft_Quadrant', TopLeft_quadrant)
    cv2.imshow('TopRight_Quadrant', TopRight_quadrant)
    cv2.imshow('BottomLeft_Quadrant', BottomLeft_quadrant)
    cv2.imshow('BottomRight_Quadrant', BottomRight_quadrant)

    # Wait for a key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
