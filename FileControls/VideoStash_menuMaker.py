import os, shutil



def makingMenu(subdirpath):

	cur_path = os.path.dirname(subdirpath) # get current path
	fileTree = os.walk(cur_path) # getting all the files in all the directories and subdirectories in current path
	menu_folder = "menu"
	os.mkdir(menu_folder)
	pictures = []

	for dirname, subdir, files in fileTree:
		basename = os.path.basename(dirname)


		for file in files:
			fileType = file.split(".")[-1]
			if fileType == "jpg":
				pictures.append(file)  # finding the pictures and put their "pathways" into the list for further ues

		for file in pictures:
			filename = file.split(".")[0]
			destfile = "{}.{}".format(menu_folder + "/" + filename, fileType)
			srcfile = dirname + "/" + file
			shutil.copy(srcfile, destfile)

def loopingDir():
	cur_path = os.path.dirname(__file__)
	fileTree = os.walk(cur_path)
	for dirname, subdir, files in fileTree:
		#basename = os.path.basename(dirname)
		makingMenu(subdir)


