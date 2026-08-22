import cv2
image = cv2.imread("fortnitephoto.jpg")
height, width = image.shape[:2]
cv2.arrowedLine(image, (0, height//2), (width, height//2), (0,255,0), 2)
cv2.arrowedLine(image, (width, height//2), (0, height//2), (0,255,0), 2)
cv2.putText(image, f"Width: {width}", (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()