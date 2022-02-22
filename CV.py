import cv2
#reading image
image = cv2.imread("sahil.jpg")
sp=20
width = int(image.shape[1]*sp/100)
height = int(image.shape[0]*sp/100)
dim = (width,height)
image = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
# print("Resized",image.shape)
#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)


#image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
# print("dimensions",image.shape)


cv2.imshow("Original Image", image)


cv2.imshow("Pencil Sketch ", sketch)
cv2.waitKey(0)
