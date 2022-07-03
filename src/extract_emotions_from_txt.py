import cv2
with open('C:/Users/Dell/Desktop/Emotion-Detection-Using-Facial-Recognition/src/happy.txt','r') as f:
    img = [line.strip() for line in f]
for image in img:
    loadedImage = cv2.imread("C:/Users/Dell/Desktop/Emotion-Detection-Using-Facial-Recognition/src/images/"+image)
    cv2.imwrite("C:/Users/Dell/Desktop/Emotion-Detection-Using-Facial-Recognition/src/data_set/happy/"+image,loadedImage)
print("done writing")