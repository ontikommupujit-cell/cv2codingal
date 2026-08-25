import cv2
import matplotlib.pyplot as plt
image=cv2.imread("images/image.jpg")
while True:
    print("\n===== IMAGE PROCESSING =====")
    print("1. Sobel")
    print("2. Canny")
    print("3. Laplacian")
    print("4. Gaussian Filter")
    print("5. Median Filter")
    print("6. Quit")
    choice=input("Choose: ")
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if choice=="1":
        result=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
        result=cv2.convertScaleAbs(result)
    elif choice=="2":
        low=int(input("Low threshold: "))
        high=int(input("High threshold: "))
        result=cv2.Canny(gray,low,high)
    elif choice=="3":
        result=cv2.Laplacian(gray,cv2.CV_64F)
        result=cv2.convertScaleAbs(result)
    elif choice=="4":
        size=int(input("Kernel size: "))
        result=cv2.GaussianBlur(image,(size,size),0)
    elif choice=="5":
        size=int(input("Kernel size: "))
        result=cv2.medianBlur(image,size)
    elif choice=="6":
        break
    else:
        print("Invalid choice")
        continue
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.show()
    plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
    plt.title("Processed Image")
    plt.show()