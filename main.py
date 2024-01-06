from functions import image_check
import sys
from PIL import Image

def main():
    path = fr"image.jpg"
    # check if path is to image file
    rect = image_check(path)
    print(rect)
    

 










if __name__ == "__main__":
    main()