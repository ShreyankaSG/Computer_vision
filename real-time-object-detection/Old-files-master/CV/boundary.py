import cv2 as cv
import matplotlib.pyplot as plt
image = cv.imread('maskresult.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
#_,binary = cv.threshold(gray, 225, 225, cv.THRESH_BINARY_INV)
binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
image = cv.drawContours(image, contours, -1, (0,255,0), 3)

plt.imshow(image)
plt.show()

 
 
