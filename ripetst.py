import cv2
import matplotlib.pyplot as plt
import numpy as np

# Function to show images
def show(image):
    plt.figure(figsize=(15, 15))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Function to detect ripeness
def detect_ripeness(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the hue for ripe fruit
    lower_bound = np.array([20, 100, 100])  # Adjust these values for your specific fruit
    upper_bound = np.array([40, 255, 255])  # Adjust these values for your specific fruit

    # Threshold the image to get the ripe fruit region
    ripe_mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Find contours in the mask
    contours, _ = cv2.findContours(ripe_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a list to store bounding boxes and ripeness percentages
    fruit_data = []

    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Calculate ripeness percentage (just a placeholder, you should replace this)
        # For demonstration purposes, we're assuming a fixed ripeness percentage.
        ripeness_percentage = 80.0

        # Append bounding box and ripeness percentage to the list
        fruit_data.append(((x, y, w, h), ripeness_percentage))

    return fruit_data

# Load the video file
video_file = r"C:\Users\mdsng\OneDrive\Desktop\ripetest\production_id_5205595 (1080p).mp4"
cap = cv2.VideoCapture(video_file)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, None, fx=1/3, fy=1/3)

    # Perform ripeness detection
    fruit_data = detect_ripeness(frame)

    # Draw bounding boxes and ripeness percentages
    for bbox, ripeness_percentage in fruit_data:
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Ripeness: {ripeness_percentage:.2f}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    show(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
