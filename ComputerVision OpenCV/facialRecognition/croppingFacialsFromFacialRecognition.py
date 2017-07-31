#adding in the pillow library for image cutting (crop)
from PIL import Image 
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

imagePath = "./imgs/graduation2.png"
image = cv2.imread(imagePath)

faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors = 6, minSize=(30,30),
	flags=cv2.CASCADE_SCALE_IMAGE)

cv2.rectangle(image, (10, image.shape[0]-20), (110,image.shape[0]), (0,0,0), 1)
cv2.putText(image, "Found ' " + str(len(faces)) + " ' Faces.", (10,image.shape[0]-5),\
 cv2.FONT_HERSHEY_SIMPLEX, 0.5,	(255,255,255), 2)

count = 0
for x, y, w, h in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (128,255,0), 2)
	#heres where the pillow comes in to save the day~~~
	faceImagePath = "./facialImages/face" + str(count) + ".png"
	foundFace = Image.open(imagePath)
	foundFace1 = foundFace.crop((x, y, x+w, y+h))
	foundFace = foundFace1.resize((200,200), Image.ANTIALIAS)
	foundFace.save(faceImagePath)
	count+=1

cv2.namedWindow("Facial Recognition", cv2.WINDOW_NORMAL)
cv2.imshow("Facial Recognition", image)
cv2.waitKey(0)
print("Facial Images Saved at : ./facialImages")
cv2.destroyWindow("Facial Recognition")
