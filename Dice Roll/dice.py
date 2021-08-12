import cv2
import random 
def diceroll():
 
 img=cv2.imread('1.png')
 img1=cv2.imread('2.png')
 img2=cv2.imread('3.png')
 img3=cv2.imread('4.png')
 img4=cv2.imread('5.png')
 img5=cv2.imread('6.png')
 number=[img,img1,img2,img3,img4,img5]
 random_array_item=random.choice(number)
 cv2.imshow('Dice',random_array_item)
 cv2.waitKey()

diceroll()