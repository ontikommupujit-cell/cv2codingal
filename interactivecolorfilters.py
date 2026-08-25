import cv2
import numpy as np
def apply_color_filter(image,filter_type):
    """Apply the specified color filter to the image"""
    filtered_image=image.copy()
    if filter_type=='red tint':
         filtered_image[:,:,1]=0
         filtered_image[:,:,0]=0
    elif filter_type =='blue tint':
         filtered_image[:,:,1]=0
         filtered_image[:,:,2]=0
    elif filter_type=='green tint':
         filtered_image[:,:,0]=0
         filtered_image[:,:,2]=0
    elif filter_type =='increase red':
         filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
    elif filter_type=='decrease blue':
         filtered_image[:,:,0]=cv2.subtract(filtered_image[:,:,0],50)
    return filtered_image
image_path='fortnitephoto.jpg'
image=cv2.imread(image_path)
if image is None:
     print('Error:Image not found')
else:
     filter_type='original'
     print('Press the following keys to apply filters')
     print('r=red tint')
     print('b=blue tint' )
     print('g=green tint')
     print('i=increase red intensity')
     print('d=decrease blue intensity')
     print('q=quit')
while True:
     filtered_image=apply_color_filter(image,filter_type)
     cv2.imshow('filtered image',filtered_image)
     key=cv2.waitKey(0)&0xFF
     if key==ord('r'):
        filter_type='red tint'
     elif key==ord('b'):
        filter_type='blue tint'
     elif key==ord('g'):
        filter_type='green tint'
     elif key==ord('i'):
        filter_type='increase red'
     elif key==ord('d'):
        filter_type='decrease blue'
     elif key==ord('q'):
        print('exiting')
        break 
     else:
         print('invalid key, enter r b g i d or q')
cv2.destroyAllWindows()

    








