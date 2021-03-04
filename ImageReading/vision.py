import cv2
import os

for x in os.listdir('.'):
    if x.endswith('.jpg'):
        images = cv2.imread(x)
        resized_images = cv2.resize(images,(100,100))
        cv2.imwrite("resized_"+x, resized_images)
        print(resized_images.shape)

