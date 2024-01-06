import re
import requests

def image_check(path: str)-> tuple:
    """
    Input: path to image file
    Function determines if the input is a valid image file
    """
    if re.search("(?i)\.(jpg|png|webp|bmp|dib|jpeg|jpg|jpe|jp2|pbm|pgm|ppm|pxm|pnm|sr|ras|tiff|tif|exr|hdr|pic)$",path):
        pass
    else:
        raise ValueError("Input valid image file.")
    

    