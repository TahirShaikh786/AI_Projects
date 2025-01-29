import cv2
import imutils # Resize

img = cv2.imread('C:\\Tahir\\TP\\Learning\\AI\\Images\\bug.jpg')
resizedImg = imutils.resize(img, width=200) # Resize Process

cv2.imshow("Original Img", img)
cv2.imshow("Resized Img", resizedImg)

# Wait for a key event before closing the windows
cv2.waitKey(0)  # Wait indefinitely for a key press

# Destroy all OpenCV windows after key press
cv2.destroyAllWindows()