import cv2

img = cv2.imread('C:\\Tahir\\TP\\Learning\\AI\\Images\\bug.jpg')

# dst = cv2.GaussianBlur(src, (kernal), borderType)
# Kernal means Smothening value
guassianImg = cv2.GaussianBlur(img, (21, 21), 0)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', guassianImg)

cv2.waitKey(0)
cv2.destroyAllWindows()