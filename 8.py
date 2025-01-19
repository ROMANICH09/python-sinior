import cv2
import numpy as np

# Create a blank white canvas
canvas = np.ones((500, 500, 3), dtype="uint8") * 255

# Draw the house base
cv2.rectangle(canvas, (150, 250), (350, 450), (150, 75, 0), -1)  # Brown rectangle

# Draw the roof
points = np.array([[150, 250], [350, 250], [250, 150]])
cv2.fillPoly(canvas, [points], (0, 0, 255))  # Red triangle

# Draw the door
cv2.rectangle(canvas, (225, 350), (275, 450), (100, 50, 0), -1)  # Dark brown rectangle

# Draw windows
cv2.rectangle(canvas, (175, 275), (215, 315), (255, 255, 0), -1)  # Yellow window
cv2.rectangle(canvas, (285, 275), (325, 315), (255, 255, 0), -1)  # Yellow window

# Show the image
cv2.imshow("House", canvas)
