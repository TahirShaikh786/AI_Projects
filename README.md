#                                                        Computer-Vision

### Some Packages to Work with Computer Vision 
>1. pip install opencv-python opencv-contrib-python
>2. pip install matplotlib
>3. pip install seaborn
>4. pip install scipy
>5. pip install imutils
>6. pip install pyautogui

### Computer Vision Library
>1. Opencv :- OpenCv is a Free, Open-source computer vision library used for tasks like image and video analysis.

>2. Pillow :- Pillow is a python library used for working with images, It allows you to open, manipulate, and save various image file formats. Whether you want to resize, enhance, or convert imagesd, Pillow makes it easy. It's like a digital toolkit for images editing in python.

>3. Scikit image :- It provides a wide range of functions and tools to work with images, including tasks like filtering, segmentation, and feature extraction.

>4. SciPy (Scitific-Python) :- SciPy is a Python Library used for scientific and technical computing. It provides a wide range of functions and tools for tasks like numerical Integration, Optimization, signal processing, and more. think of it as a Swiss Army knife for Scientific and engineering calculations in Python.

>5. NumPy (Numerical-Python) :- NumPy is a Python Library for numerical computations. It Offers a Powerfull array object call "ndarray" that allows yout to perform mathematical operations on large datasets effieciently. Think of it as the go-to-toolbox for number crunching and data manipulation in Python.

### Application of Computer Vision
>1. Moving Object Recognition
>2. Face Recognition
>3. Autonomous Vehicle
>4. Emotion Recognition

## Projects
> 1. [Moving Object Recognition](./Computer%20Vision/Moving_Object_Recognition/app.py) is a technique used in Computer Vision & image processing. Multiple consecutive frames from a video are compared by various methods to determine if any moving object is detected.<br />Components of This:- <br />1. [Resize Img](./Computer%20Vision/Moving_Object_Recognition/Components/resize.py)<br />2. [Blur & Smooth image](./Computer%20Vision/Moving_Object_Recognition/Components/Gaussian_Blur_Smootening.py)<br />3. [Threshold Img](./Computer%20Vision/Moving_Object_Recognition/Components/Threshold_img.py)<br />4. [Drawing Rectangle & Putting Text & Finding Contours](./Computer%20Vision/Moving_Object_Recognition/Components/Drawing_Putting_img.py)<br />

>2. [Object Detection & Tracking Based on Color](./Computer%20Vision/Object%20Detection%20Based%20On%20Color/app.py) :- it's task is that to check video Surveillance and vehicle navigation. Image Processing is method of extracting some useful information by converting image into digital inform by perfoming some operations on it.
> [Block Diagram of tracking Color Object](./Images/Block%20Diagram%20of%20tracking%20Color%20Object.png)
> What is HSV Value
>     - HSL & HSV are alternative representations of the RGB color model, designed in the 1970s by computer graphics researchers to more closely align with the way human vision perceives color-making attributes.
>     - HSV Color Space. the HSV color space (hue, saturation, value) is often used by people who are selecting colors (e.g. of paints or inks) from a color wheel or palette, because it corresponds better to how people experience color than the RGB color space does.
>
>     - BGR to HSV
>       #dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
>       hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
>
>     - Minimum Enclosing Circle
>       #((x, y), radius) = cv2.minEnclosingCircle(contourArea)
>       ((x, y), radius) = cv2.minEnclosingCircle(c)
>
>     - Moments to find center of the Area :- Image moments help you to calculate some features like center of mass of the object, area of the object, etc.
>       #var = cv2.moments(contourArea)
>       M = cv2.moments(c)
>       [center Formula](./Images/center.png)
>
>     - Drawing Circle
>       # cv2.circle(src, (x, y), int(radius), color, thickness)
>        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
>        cv2.circle(frame, center, 5, (0, 0, 255), -1)