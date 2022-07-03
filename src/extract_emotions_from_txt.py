import cv2
with open('C:/Users/hp/OneDrive/Desktop/Emotion-Detection-Using-Facial-Recognition/src/sad.txt','r') as f:
    img = [line.strip() for line in f]
for image in img:
    loadedImage = cv2.imread("C:/Users/hp/OneDrive/Desktop/Emotion-Detection-Using-Facial-Recognition/src/images/"+image)
    cv2.imwrite("C:/Users/hp/OneDrive/Desktop/Emotion-Detection-Using-Facial-Recognition/src/data_set/sad/"+image,loadedImage)
print("done writing")