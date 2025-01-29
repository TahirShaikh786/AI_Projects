# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2 # opencv-python

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # Loading Algorithm
print(haar_cascade.empty())  # Should print 'False' if the classifier loaded successfully

cam = cv2.VideoCapture(0) # Intializing Camera ID

while True:
  _ , img = cam.read() # Reading frame from camera

  if img is None:
    print("Error: Unable to capture image.")
    break

  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting color image to grayscale image
  faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4) # Getting Co-Ordinates

  for(x, y, h, w) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 9) # Drawing Rectangle
  
  cv2.imshow("FaceDetection", img) # Display the Frame

  key = cv2.waitKey(10)
  print(key) # Optional

  if key == 27: #Escape key to Exit
    break

cam.release()
cv2.destroyAllWindows()