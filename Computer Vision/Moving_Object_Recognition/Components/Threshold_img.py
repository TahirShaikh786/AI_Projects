#  Threshold means to create a Sketch of an image
# Note :- To Create a Sketch of a Img Firstt we have to Convert Img into GrayScale
#  The Higher the threshold value the complete sketch will be given

import cv2

img = cv2.imread('C:\\Tahir\\TP\\Learning\\AI\\Images\\bug.jpg')

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# dst = cv2.threshold(src, thresholdVal, maxThresholdVal, binaryType)[1]
thresholdImg = cv2.threshold(grayImg, 180, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Original", img)
cv2.imshow("Threshold", thresholdImg)

cv2.waitKey(0)
cv2.destroyAllWindows()