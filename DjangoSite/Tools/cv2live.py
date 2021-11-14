import cv2 
import shutil
import random

def getCapture():
    addition = random.randrange(start=1, stop=999)
    file = 'capture' + str(addition) + '.jpg'
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    resized_image = cv2.resize(frame, (224, 224)) 
    cv2.imwrite(filename=file, img=resized_image)
    webcam.release()
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    shutil.move(file, r"C:\Users\kanis\Desktop\clonedlmao\DjangoSite\media")
    return file
