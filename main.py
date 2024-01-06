from functions import image_check
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
 

def main():
    path = fr"image.jpg"
    # check if path is to image file
    image_check(path)
    # converts the image to a numpy array
    image = cv.imread(path)
    #return's the place where we selected the ROI on the array image
    cv.namedWindow('Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Image',width,heigth)
    cv.selectROI("Image",image)










if __name__ == "__main__":
    main()