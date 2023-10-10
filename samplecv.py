#Importing the OpenCV library
import cv2

#Reading the image using imread() function
image = cv2.imread('cat.png')

#Extract height and width of image
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

#Extracting RBG Values
#randomly choosing a pixel by passing 100, 100 for h and w
(B, G, R) = image[100, 100]

#Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

#pass channel to extract the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

#calculate the region of interest by slicing pixels of the image
roi = image[100 : 500, 200 : 700]

#resize() function takes 2 parameters
#the image and the dimensions
resize = cv2.resize(image, (800, 800))
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

cv2.imshow("image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()








