# video camra that can take lotsa pictures 
import cv2, os, os.path

if not os.path.exists("./camera"):
	os.mkdir('camera')

cv2.namedWindow("Camera")
cam = cv2.VideoCapture(0)

count = 0
def menu():
	print("** Press Enter to take pictures **")
	print("** Press 'Q' or 'q' to Quit **" )
	print('==================================')


menu()
while cam.isOpened():
	success, img = cam.read()
	if success:
		cv2.imshow("Camera", img)
		k = cv2.waitKey(1) # a short term wait, to keep camera running smoothly
		#remember it returns ASCII code, so use the ord() python function
		if k == ord('\r'):
			count+=1
			cv2.imwrite("./camera/picture{}.jpg".format(count), img)
			print("Picture Saved!")
			print('==============')
			menu()
		elif k == ord("q") or k == ord("Q"):
			print("Bye!~")
			break
		
cam.release()
cv2.destroyAllWindows()
