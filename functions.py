import re
import requests
from PIL import Image
import cv2 as cv

def image_check(path: str)-> list:
    if re.search("(?i)\.(jpg|png|webp|bmp|dib|jpeg|jpg|jpe|jp2|pbm|pgm|ppm|pxm|pnm|sr|ras|tiff|tif|exr|hdr|pic)$",path) == False:
        raise ValueError("Input valid image file.")
    with Image.open(path) as file:
        width, heigth = file.size
    image = cv.imread(path)
    cv.namedWindow('Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Image',width,heigth)
    return cv.selectROI("Image",image)

    