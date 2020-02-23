import glob
import cv2

img = glob.glob('*.jpeg')

#img = [cv2.imread('images.jpg',0),cv2.imread('img.jpeg',0),cv2.imread('img2.jpeg',0),cv2.imread('i.jpeg',0),cv2.imread('p1.jpeg',0)]

for i in img:
    im = cv2.imread(i,0)
    rimg = cv2.resize(im,(1600,900))
    cv2.imwrite(f'new{i}.jpg',rimg)