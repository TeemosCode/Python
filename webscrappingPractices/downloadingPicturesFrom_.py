import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.tooopen.com/img/87.aspx"

html = requests.get(url)
html.encoding = "utf-8"

bs = BeautifulSoup(html.text, "html.parser")

#creating directories to save the pictures
images_dir = "images/"
if not os.path.exists(images_dir):
	os.mkdir(images_dir)

#grabbing all the <a> and <img> tags
all_links = bs.find_all(["a","img"])
for link in all_links:
	#getting the contents of the tags
	src = link.get("src")
	href = link.get("href") 
	# they are strings of paths of the images
	attrs=[src, href]

	for attr in attrs:
		#reading .jpg and .png files
		if attr != None and (".jpg" in attr or ".png" in attr):
			#set full image path
			full_path = attr
			filename = full_path.split('/')[-1] # the image name
			extname = filename.split('.')[-1] # the sub file name
			filename = filename.split('.')[-2] # the image file name only

			if "jpg" in extname:
				filename = filename + ".jpg"
			else:
				filename = filename + ".png"

			print(filename)
			#saving the files, in case some are unauthorized, use try and except
			try:
				image = urlopen(full_path) # use read() method later on for the real goody inside the image object
				f = open(os.path.join(images_dir, filename), 'wb')
				f.write(image.read())
				f.close()
			except:
				print(" {} Access Denied!".format(filename))

