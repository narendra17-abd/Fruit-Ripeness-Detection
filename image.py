import cv2
import numpy as np

# Function to detect fruit ripeness based on color
def detect_ripeness(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert image to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for the color of ripe fruit
    lower_ripe = np.array([140, 70, 50])  # Adjust these values based on your specific fruit color
    upper_ripe = np.array([180, 255, 255])
    
    # Create a mask for ripe fruit
    mask_ripe = cv2.inRange(hsv, lower_ripe, upper_ripe)
    
    # Count the number of non-zero pixels in the mask
    ripe_pixel_count = np.count_nonzero(mask_ripe)
    
    # Assuming a simple threshold: If more than 1000 pixels are ripe, consider it ripe
    if ripe_pixel_count > 1000:
        return "Ripe"
    else:
        return "Unripe"

# Example usage
image_path = r"C:\Users\mdsng\OneDrive\Desktop\ripetest\blueberry.jpeg"  # Provide the path to your fruit image
ripeness = detect_ripeness(image_path)

print('Predicted fruit ripeness:', ripeness)
