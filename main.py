import cv2
from datetime import datetime


def take_picture(name):
    cap = cv2.VideoCapture(0)
    retval, frame = cap.read()
    cv2.flip(frame, 1, frame)
    cv2.imwrite(name, frame)
    cap.release()


def main():
    extension = '.png'
    imgdir = "C:\\LoginImgs\\imgs\\"
    filename = "{0}{1}{2}".format(imgdir, datetime.now().strftime("%Y%m%d-%H%M%S"), extension)
    take_picture(filename)


main()
