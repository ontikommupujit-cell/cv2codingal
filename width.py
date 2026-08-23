import cv2
image = cv2.imread("fortnitephoto.jpg")
height, width = image.shape[:2]
cv2.rectangle(image, (100, 100), (300, 300), (0, 255, 0), 2)
cv2.circle(image, (400, 200), 50, (255, 0, 0), 2)
cv2.line(image, (50, 400), (500, 400), (0, 0, 255), 2)
cv2.arrowedLine(image, (0, height//2), (width, height//2), (0,255,0), 2)
cv2.arrowedLine(image, (width, height//2), (0, height//2), (0,255,0), 2)
cv2.putText(image, f"Width: {width}", (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()