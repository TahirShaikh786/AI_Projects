""" 
********************************************* Drawing Rectangle *********************************************
cv2.rectangle(src, startpoint, endpoint, color, thickness)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

******************************************** Putting Text in Image ******************************************
cv2.putText(src, text, position, font, fontSize, color, thickness)
cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

******************************************** Finding Contours ***********************************************
It basically find all the neighbours point and make a single image

dst = cv2.findContours(src, contourRetrievalMode, contourApproximationMethod)
cnts = cv2.findContours(threshing.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
"""