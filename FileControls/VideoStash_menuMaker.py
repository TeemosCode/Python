import os, shutil, glob



def makingMenu(path):

	
	os.chdir(path) # getting all the files in all the directories and subdirectories in current path
	menu_folder = "zzzzzMENUzzzzz" #somehow stops at the menu itself
	if not os.path.exists(menu_folder):
		os.mkdir(menu_folder)
		print("making dir")
	pictures = []
	#print(path)
	dirs = os.listdir(path)

	#print(dirs)
	
	for directory in dirs:
		#print(directory)
		files = glob.glob(path + "/" + directory + "/*.jpg")
		print(files)
		print("asdfasdfasdf123409810-91--______+++++___+++")
		#os.chdir(directory)
		
		"""
		files = os.listdir(directory)
		for file in files:
			#if subdir != "[]" or subdir != menu_folder:
			#basename = os.path.basename(dirname)
			#print(dirname, subdir, files)

			print(file)
			fileType = file.split(".")[-1]
			#print(fileType)
			if fileType == "jpg":
				pictures.append(file)  #finding the pictures' names
				#print(pictures)
		"""
	#print(pictures)
		for file in files:
			if file == "[]" or file == None:
				continue
			print("\n=====")
			print(file)
			print("\n =====")
			destfile = path + '/' + menu_folder + "/" + file.split("/")[0]
			srcfile = file
			#print(destfile)
			#print(srcfile)
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

