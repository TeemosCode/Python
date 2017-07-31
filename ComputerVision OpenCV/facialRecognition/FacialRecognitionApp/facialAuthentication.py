#creating a program to authenticate users through facial recognition
import cv2, os, math, operator, os.path
from PIL import Image
from functools import reduce

if not os.path.exists('./authenticateFaces'):
	os.mkdir("authenticateFaces")
if not os.path.exists('./loginFaces'):
	os.mkdir("loginFaces")

def printMenu():
	print("""
		  --------------------------------------
		  ** Press 'Enter' for picture taking **
		  ** Press 'q' or 'Q' to quit **
		  --------------------------------------
		  """)

#need cropping for both indexing and authenticating picture taking, make them diferent by inputing different directory path
def cropAuthenticateFace(user, dirc):
	img = cv2.imread(dirc+user+".jpg")

	faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors = 6, minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
	for x, y, w, h in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (128,255,0), 2)
		image = Image.open(dirc+user+".jpg")
		image2 = image.crop((x,y,x+w,y+h))
		image = image2.resize((200,200), Image.ANTIALIAS)
		image.save(dirc+user+".jpg")



def facialAuthentication(user):
	print("Authenticating\n...\n...\n...\n...\n...")
	loginface = Image.open('./loginFaces/'+user+'.jpg')
	authenticateFace = Image.open('./authenticateFaces/' + user + '.jpg')
	h1 = loginface.histogram()
	h2 = authenticateFace.histogram()
	# the authentication algorithm
	diff = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, h1, h2)))/len(h1))
	#diff value to decide whether its the same, similar picture or not : the smaller the value the closer the images
	if diff <= 100:
		print("===\nPassed Authentication! Welcome!\n===\ndiff = %4.2f" % diff)
	else:
		print("===\nFAILED Authentication! You are NOT authorized!\n===\ndiff = %4.2f" % diff)



while True:
	print("------------------\nWelcome to Facial Authentication\n------------------")
	user = input("Please input your name: ['Q' or 'q' or Any input with spaces to quit] \n-->")
	if user.lower() == "q" or ' ' in user or user == '':# incase ppl stuff up the program with unwanted input strings
		print("Bye~~Bye~~")
		break
	userface = user + '.jpg'

	#if users face doesn't exist in the authentiacation folder, turn on the camera to take a picture for indexing
	if not os.path.exists('./authenticateFaces/' + userface):
		printMenu()
		print("========Indexing Camera for future Authentication=======")
		cv2.namedWindow("IndexingCamera")
		cam = cv2.VideoCapture(0) # turn on camera
		while cam.isOpened():
			success, img = cam.read() # the magic of opencv camera hehe
			if success:
				cv2.imshow("IndexingCamera", img)
				key = cv2.waitKey(1) # wait for useing input, (self reminder, its ASCII!)
				if key == ord('\r'):
					instantImg = img #is this necessary?
					cv2.imshow("IndexingCamera", instantImg) # shows the image, freeze it so user can take time to look and decide whooohoo~~~
					check = input("Are you sure you want this picture as your index? ['y' for yes/'n' for no]")
					while check not in ['y',"Y","n","N"]:
						print("Invalid Choice.")
						check = input("Are you sure you want this picture as your index? ['y' for yes/'n' for no]")
					if check.lower() == 'y':
						cv2.imwrite("./authenticateFaces/" + userface, instantImg)#save to path, the camera instant img
						#crop the face through facial recognition 
						cropAuthenticateFace(user, "./authenticateFaces/")

						print("Image Saved, Indexed!\n")
						break
				elif key == ord('q') or key == ord('Q'):
					print("Okay then..... Bye!")
					break
			else:
				print("Cannot successfully access the camera!\n Nothing we can do until you fix it :)")
				break
		cam.release()
		cv2.destroyWindow("IndexingCamera")
	#else if the person already has his picture (username.jpg) indexed, open the login camera window
	else:
		print("========Login Camera for Authentication=======")
		cv2.namedWindow("Login")
		printMenu()
		cam = cv2.VideoCapture(0)
		while cam.isOpened():
			success, img = cam.read()
			if success:
				cv2.imshow("Login", img)
				key = cv2.waitKey(1)
				if key == ord('\r'):
					cv2.imwrite("./loginFaces/" + user + '.jpg', img)
					#crop the face out too
					cropAuthenticateFace(user, "./loginFaces/")
					print("Image Saved!\n----")
					facialAuthentication(user) # Check the program to authenticate the picture with the user indexed picture
					
					break
				elif key == ord('q') or key == ord('Q'):
					print("Unable to Authenticate without a picture, Access Denied!")
					break
		cam.release()
		cv2.destroyWindow("Login")




