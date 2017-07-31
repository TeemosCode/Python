#using builtin pc camera to capture pictures
import cv2, os, os.path

if not os.path.exists('./camera'):
	os.mkdir("camera")

cv2.namedWindow("Camera")


cam = cv2.VideoCapture(0) # 0 : built-in camera, turn it on
#count = 0
while cam.isOpened():
	readsuccess, img = cam.read()
	if readsuccess == True:
		cv2.imshow("Camera", img)
		print("Choose 'enter' for taking and saving picture. Choose 'q' or 'Q' to quit")
		print('========================================================================')
		k = cv2.waitKey(1) # reads in the ASCII code of the button the user pushes lol (it returns an ASCII code!)
		if k == ord("a") or k == ord("A") or k == ord('\r'):
			#count+=1
			cv2.imwrite("./camera/picture.jpg", img)
			print("picture saved\n-----------------")
			break
cam.release()
cv2.waitKey(0)
cv2.destroyAllWindows()



