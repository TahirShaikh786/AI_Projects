import cv2 # opencv
import time # delay
import imutils # resize

cam = cv2.VideoCapture(0) # Cam Id
time.sleep(1)

firstFrame = None
area = 500

while True:
  _, img = cam.read() # read from the camera ret, Img
  text = "Normal"

  img = imutils.resize(img, width=800) # Reize

  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert img to grayScale Img

  guassianImg = cv2.GaussianBlur(grayImg, (21, 21), 0) # Smoothened

  if firstFrame is None:
    firstFrame = guassianImg # Capturing the First frame
    continue

  imgDiff = cv2.absdiff(firstFrame, guassianImg) # absolute Difference

  threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

  # To Increase the Thickness is called Dilation
  threshImg = cv2.dilate(threshImg, None, iterations=2) # left overs-erotion or dilation

  cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # make Complete Contours
  
  cnts = imutils.grab_contours(cnts)

  for c in cnts:
    if cv2.contourArea(c) < area: # make Full area
      continue
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0 , 255, 0), 2)
    text = "Moving Object Detected"
  # print(text)

  cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
  cv2.imshow("CameraFeed", img)

  key = cv2.waitKey(10)
  if(key == ord('q')):
    break

cam.release()
cv2.destroyAllWindows()