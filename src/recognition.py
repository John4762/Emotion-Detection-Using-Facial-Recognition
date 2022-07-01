
from os import path
import cv2
import numpy as np
from file_selector import file_select

from path_generalizer import path_finder

x=path_finder()
p1=path.join(x,'trainer','trainer.yml')
#toCheck
print(p1)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(p1)
cascadePath = path.join(x,'haarcascade_frontalface_default.xml')
#toCheck
print(cascadePath)
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# Emotions related to ids: example ==> Anger: id=0,  etc
names = ['Happy', 'Sad', 'None', 'None', 'None', 'None'] 

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#ret, img =cam.read()
pic=file_select()
img = cv2.imread(pic)
#img = cv2.flip(img, 0) # Flip vertically

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale( 
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (int(minW), int(minH)),
    )

for(x,y,w,h) in faces:

    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

    # Check if confidence is less them 100 ==> "0" is perfect match 
    if (confidence < 100):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))
    
    cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
   # cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  


p2=file_select()
#toCheck

cv2.imwrite(p2,img) 

print("\n [INFO] Done detecting and Image is saved")
cam.release()
cv2.destroyAllWindows()
