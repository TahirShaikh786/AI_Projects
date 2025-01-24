import cv2  # importing Computer Vision = OpenCV Library = cv2

# Read the image using OpenCV library
image = cv2.imread("C:\\Tahir\\TP\\Learning\\AI\\Images\\bug.jpg")

# Convert the image from RGB to BGR
BGR = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
GRAY = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Display the original and converted images
cv2.imshow('original', image)
cv2.imshow('BGR', BGR)
cv2.imshow('GRAY', GRAY)

# Wait for a key event before closing the windows
cv2.waitKey(0)  # Wait indefinitely for a key press

# Destroy all OpenCV windows after key press
cv2.destroyAllWindows()
