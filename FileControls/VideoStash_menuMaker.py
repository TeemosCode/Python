import os, shutil



def makingMenu(path):

	
	os.chdir(path) # getting all the files in all the directories and subdirectories in current path
	menu_folder = "menu"
	if not os.path.exists(menu_folder):
		os.mkdir(menu_folder)
		print("making dir")
	pictures = []
	print(path)
	fileTree = os.walk(path)
	for dirname, subdir, files in fileTree:

		#if subdir != "[]" or subdir != menu_folder:
		#basename = os.path.basename(dirname)
		print(files)
		#print(dirname, subdir, files)

		for file in files:
			fileType = file.split(".")[-1]
			#print(fileType)
			if fileType == "jpg":
				pictures.append(file)  #finding the pictures' names
				#print(pictures)
		for file in pictures:
			print(file)
			destfile = path + '/' + menu_folder + "/" + file
			srcfile = subdir + "/" + file
			print(destfile)
			print(srcfile)
			'''
			destfile = "{}.{}".format(menu_folder + "/" + file)
			srcfile = dirname + "/" + file
			'''
			shutil.copy(srcfile, destfile)
	#os.chdir(parentpath)

def loopingDir():
	cur_path = os.getcwd()
	
	fileTree = os.walk(cur_path)
	#print("hello")
	for dirname, subdir, files in fileTree:
		#print(dirname, subdir, files)
		for dirnames in subdir:
			path = cur_path + '/' + dirnames
			#basename = os.path.basename(dirname)
			try:
				makingMenu(path)
			except:
				continue

loopingDir()

