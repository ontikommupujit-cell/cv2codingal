import cv2
import matplotlib.pyplot as plt
image=cv2.imread("fortnitephoto.jpg")
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
bright=rotated+50
cropped=bright[100:500,100:500]
plt.imshow(cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB))
plt.show()
cv2.imwrite("edited.jpg",cropped)