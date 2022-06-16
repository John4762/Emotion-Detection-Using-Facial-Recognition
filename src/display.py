import cv2
import matplotlib.pyplot as plt


image = cv2.imread("C:/Users/hp/OneDrive/Documents/GitHub/S6 MiniProject/Emotion-Detection-Using-Facial-Recognition/src/generated_elon.jpg")
height, width = image.shape[:2]
resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

fig = plt.gcf()
fig.set_size_inches(18, 10)
plt.axis("off")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()