"""Import stuff goes here"""
import numpy as np
import cv2

"""Image loader stuff goes here"""
def load_img(path, channel):
    """Image loader functionality goes here. Channels:
    1 = color image
    0 = greyscale image
    -1 = unchanged image
    """
    img = cv2.imread(path, channel)
    return img


def show(title, img):
    """show image"""
    for i in range(len(title)):
        cv2.imshow(title[i],img[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""Preprocessing stuff goes here. Neccesseray steps: binarize and erode"""
def make_binary(img):
    """convert image to binary"""
    (thresh, b_img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('treshold: ',thresh)
    return b_img

def erode_img(img):
    """erode the image with a given kernel"""
    kernel = np.ones((1,1),np.uint8)
    er_img = cv2.dilate(img,kernel,iterations=1)
    return er_img

if __name__ == '__main__':
   path = 'img/mean.png'
   img  = load_img(path, 0)
   #make binary
   b_img = make_binary(img)
   #erode
   er_img = erode_img(b_img)
   #show all
   show(['original','binary','eroded'], [img,b_img,er_img])

