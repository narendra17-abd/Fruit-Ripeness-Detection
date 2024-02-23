import cv2
import numpy as np

# Function to detect fruit ripeness based on color
def detect_fruit_ripeness(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert image to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for the color of ripe fruits
    # These values are approximate and may need further adjustment

    # Ripe apple
    lower_ripe_apple = np.array([0, 50, 50])
    upper_ripe_apple = np.array([10, 90, 90])

    # Ripe banana
    lower_ripe_banana = np.array([30, 100, 100])
    upper_ripe_banana = np.array([60, 255, 255])

    # Ripe strawberry
    lower_ripe_strawberry = np.array([140, 70, 50])
    upper_ripe_strawberry = np.array([180, 255, 255])

    # Ripe orange
    lower_ripe_orange = np.array([10, 100, 20])
    upper_ripe_orange = np.array([30, 255, 255])

    # Ripe blueberry
    lower_ripe_blueberry = np.array([100, 50, 50])
    upper_ripe_blueberry = np.array([140, 255, 255])

    # Ripe lemon
    lower_ripe_lemon = np.array([20, 100, 100])
    upper_ripe_lemon = np.array([40, 255, 255])

    # Ripe mango
    lower_ripe_mango = np.array([20, 100, 100])
    upper_ripe_mango = np.array([45, 255, 255])

    # Ripe grape
    lower_ripe_grape = np.array([110, 50, 50])
    upper_ripe_grape = np.array([140, 255, 255])

    # Ripe kiwi
    lower_ripe_kiwi = np.array([60, 100, 100])
    upper_ripe_kiwi = np.array([85, 255, 255])

    # Ripe watermelon
    lower_ripe_watermelon = np.array([0, 100, 100])
    upper_ripe_watermelon = np.array([10, 255, 255])


    # Create a mask for each ripe fruit
    mask_ripe_apple = cv2.inRange(hsv, lower_ripe_apple, upper_ripe_apple)
    mask_ripe_banana = cv2.inRange(hsv, lower_ripe_banana, upper_ripe_banana)
    mask_ripe_strawberry = cv2.inRange(hsv, lower_ripe_strawberry, upper_ripe_strawberry)
    mask_ripe_orange = cv2.inRange(hsv, lower_ripe_orange, upper_ripe_orange)
    mask_ripe_blueberry = cv2.inRange(hsv, lower_ripe_blueberry, upper_ripe_blueberry)
    mask_ripe_lemon = cv2.inRange(hsv, lower_ripe_lemon, upper_ripe_lemon)
    mask_ripe_mango = cv2.inRange(hsv, lower_ripe_mango, upper_ripe_mango)
    mask_ripe_grape = cv2.inRange(hsv, lower_ripe_grape, upper_ripe_grape)
    mask_ripe_kiwi = cv2.inRange(hsv, lower_ripe_kiwi, upper_ripe_kiwi)
    mask_ripe_watermelon = cv2.inRange(hsv, lower_ripe_watermelon, upper_ripe_watermelon)


    # Count the number of non-zero pixels in the mask for each fruit
    ripe_pixel_count_apple = np.count_nonzero(mask_ripe_apple)
    ripe_pixel_count_banana = np.count_nonzero(mask_ripe_banana)
    ripe_pixel_count_strawberry = np.count_nonzero(mask_ripe_strawberry)
    ripe_pixel_count_orange = np.count_nonzero(mask_ripe_orange)
    ripe_pixel_count_blueberry = np.count_nonzero(mask_ripe_blueberry)
    ripe_pixel_count_lemon = np.count_nonzero(mask_ripe_lemon)
    ripe_pixel_count_mango = np.count_nonzero(mask_ripe_mango)
    ripe_pixel_count_grape = np.count_nonzero(mask_ripe_grape)
    ripe_pixel_count_kiwi = np.count_nonzero(mask_ripe_kiwi)
    ripe_pixel_count_watermelon = np.count_nonzero(mask_ripe_watermelon)


    # Assuming a simple threshold: If more than 1000 pixels are ripe, consider it ripe
    if ripe_pixel_count_apple > 100:
        return "Ripe "
    elif ripe_pixel_count_banana > 1000:
        return "Ripe "
    elif ripe_pixel_count_strawberry > 1000:
        return "Ripe "
    elif ripe_pixel_count_orange > 1000:
        return "Ripe "
    elif ripe_pixel_count_blueberry > 1000:
        return "Ripe "
    elif ripe_pixel_count_lemon > 1000:
        return "Ripe "
    elif ripe_pixel_count_mango > 1000:
        return "Ripe "
    elif ripe_pixel_count_grape > 1000:
        return "Ripe "
    elif ripe_pixel_count_kiwi > 1000:
        return "Ripe "
    elif ripe_pixel_count_watermelon > 1000:
        return "Ripe "
    else:
        return "Unripe"


# List of image paths
image_paths = [
               r"C:\Users\mdsng\OneDrive\Desktop\ripetest\unripeapple.jpeg",r"C:\Users\mdsng\OneDrive\Desktop\ripetest\banana.jpg",
               r"C:\Users\mdsng\OneDrive\Desktop\ripetest\strawberry.jpg",r"C:\Users\mdsng\OneDrive\Desktop\ripetest\orange.jpg",
               r"C:\Users\mdsng\OneDrive\Desktop\ripetest\blueberry.jpeg",r"C:\Users\mdsng\OneDrive\Desktop\ripetest\lemon.jpg",
               r"C:\Users\mdsng\OneDrive\Desktop\ripetest\mango.jpg", r"C:\Users\mdsng\OneDrive\Desktop\ripetest\grapes.jpeg",
               r"C:\Users\mdsng\OneDrive\Desktop\ripetest\kiwi.jpg", r"C:\Users\mdsng\OneDrive\Desktop\ripetest\watermelon.jpg"]

# Iterate over each image and predict ripeness
for image_path in image_paths:
    print(f'Predicted ripeness for {image_path}: {detect_fruit_ripeness(image_path)}')

