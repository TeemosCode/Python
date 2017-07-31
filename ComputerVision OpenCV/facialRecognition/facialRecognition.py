import cv2, numpy
# still needs improving on the accuracy and image sizes (still aint quit sure about it yet...)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faceCascade.load('haarcascade_frontalface_default.xml')

imagename = cv2.imread('./imgs/graduation2.png')
#imagename.shape[0] : image height, imagename.shape[1] : image width
#main detection function, returns a LIST with tuples of attributes of recognized faces : [(x, y, width, height),]
faces = faceCascade.detectMultiScale(imagename, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
 #flags=cv2.CASCADE_SCALE_IMAGE)

#create a box to put in the text
cv2.rectangle(imagename, (10, imagename.shape[0]-20), (110,imagename.shape[0]), (0,0,0), 1)
cv2.putText(imagename, "Found '" + str(len(faces)) + "'' Faces!", (10,imagename.shape[0]-5),\
 cv2.FONT_HERSHEY_SIMPLEX, 0.5,	(255,255,255), 2)

for x,y,w,h in faces:
	cv2.rectangle(imagename, (x,y), (x+w, y+h), (128,255,0), 2)

cv2.namedWindow("faceDetection", cv2.WINDOW_NORMAL)
cv2.imshow("faceDetection", imagename)
#cv2.resizeWindow("faceDetection", 800,600)   resize the window frame when displayed
cv2.waitKey(0)
cv2.destroyWindow("faceDetection")


