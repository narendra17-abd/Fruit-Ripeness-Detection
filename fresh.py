import cv2
import numpy as np

# Function to get HSV thresholds for a specific fruit
def get_fruit_threshold(fruit_name):
    fruit_thresholds = {
        'apple': (np.array([0, 50, 50]), np.array([10, 255, 255])),
        'banana': (np.array([30, 100, 100]), np.array([60, 255, 255])),
        'strawberry': (np.array([140, 70, 50]), np.array([180, 255, 255])),
        'orange': (np.array([10, 100, 20]), np.array([30, 255, 255])),
        'blueberry': (np.array([100, 50, 50]), np.array([140, 255, 255])),
        'lemon': (np.array([20, 100, 100]), np.array([40, 255, 255])),
        'mango': (np.array([20, 100, 100]), np.array([45, 255, 255])),
        'grape': (np.array([110, 50, 50]), np.array([140, 255, 255])),
        'kiwi': (np.array([60, 100, 100]), np.array([85, 255, 255])),
        'watermelon': (np.array([0, 100, 100]), np.array([10, 255, 255]))
    }

    return fruit_thresholds.get(fruit_name, None)

# Function to detect fruit ripeness based on color
def detect_fruit_ripeness(image_path, fruit_name):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert image to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the thresholds for the specified fruit
    lower_threshold, upper_threshold = get_fruit_threshold(fruit_name)
    if lower_threshold is None:
        print(f"Thresholds not available for {fruit_name}.")
        return "Unknown"

    # Create a mask for the specified fruit
    mask_fruit = cv2.inRange(hsv, lower_threshold, upper_threshold)

    # Count the number of non-zero pixels in the mask for the specified fruit
    ripe_pixel_count = np.count_nonzero(mask_fruit)

    # Assuming a simple threshold: If more than 1000 pixels are ripe, consider it ripe
    if ripe_pixel_count > 1000:
        return f"Ripe "
    else:
        return f"Unripe "

# Example usage
image_path = r"C:\Users\mdsng\OneDrive\Desktop\ripetest\mango.jpg"  # Provide the path to your fruit image
fruit_name = 'apple'  # Specify the fruit name
ripeness = detect_fruit_ripeness(image_path, fruit_name)



print(f'Predicted fruit ripeness for {fruit_name}: {ripeness}')
