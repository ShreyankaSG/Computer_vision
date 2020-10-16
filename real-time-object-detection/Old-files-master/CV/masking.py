import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('test2.png')
print('This image is:', type(image), 
      ' with dimensions:', image.shape)
image_copy = np.copy(image)

# Change color to RGB (from BGR)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Display the image copy
plt.imshow(image_copy)

lower_black = np.array([43, 43, 43])    
upper_black = np.array([43,43, 43])
mask = cv2.inRange(image_copy, lower_black, upper_black)

# Vizualize the mask
plt.imshow(mask,'gray')
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [255, 255, 255]


# Display it!

plt.imshow(mask, 'gray')
plt.show()


