import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread("../original_images/fortnitephoto.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap="gray")
plt.title("Grayscale Image")
plt.show()
cropped=image[100:300,200:400]
(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
brightness_matrix=np.ones(image.shape,dtype=np.uint8)*50
bright=cv2.add(image,brightness_matrix)
cv2.imwrite("../output_images/grayscale.jpg",gray)
cv2.imwrite("../output_images/cropped.jpg",cropped)
cv2.imwrite("../output_images/rotated.jpg",rotated)
cv2.imwrite("../output_images/brightened.jpg",bright)