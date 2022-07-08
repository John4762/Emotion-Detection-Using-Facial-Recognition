import cv2
with open('E:/BTech/S6/Mini Project/Music Recommendation System/Emotion-Detection-Using-Facial-Recognition/src/happy.txt','r') as f:
    img = [line.strip() for line in f]
for image in img:
    loadedImage = cv2.imread("E:/BTech/S6/Mini Project/Music Recommendation System/Emotion-Detection-Using-Facial-Recognition/src/images/"+image)
    cv2.imwrite('E:/BTech/S6/Mini Project/Music Recommendation System/Emotion-Detection-Using-Facial-Recognition/src/data_set/happy/'+image,loadedImage)
print("done writing")