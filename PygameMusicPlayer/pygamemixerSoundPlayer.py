#playing around with pygame, starting off with the 'mixer' object to play with the sounds and volumns.
# two properties in there. the Sound() and music. Sound() plays liks .OGG or .WAV [shorter files]. 'music' can play longer ones, including .mp3 files
'''
from pygame import mixer
mixer.init() # HAS to be initialized FIRST for it to work!

sound = mixer.Sound('wav/hit.wav')
sound.play(loop=0) #default is 0, which means 1 time. -1 means infinite amount of times till pc shuts down or ya stop it 
sound.set_volume() # 0.0~1.0
sound.get_volume()
'''
# for Unix os
from pygame import mixer
import os, glob #using glob.glob(filesToLookFor) to get a LIST of files we lookin for... use it for gettin music files we want to play
mixer.init()

sourceDir = 'music/'
soundFiles = glob.glob(sourceDir + "*.wav") # using .wav for example
fileIndex = 0
status = ''

sound = mixer.Sound(soundFiles[fileIndex])

def menu(status):
	os.system("clear")
	print(
	"""
	==================== Sound Player (wav, ogg...) ====================
	          (Please choose the choice of action to preform)
	
	1.   Play Song

	2.   Pause Song

	3.   Next Song

	4.   Prev Song

	5.   Xth Song

	0.   Quit

	==================== ========================== ====================

	""")

	print(status)
	printLine()

def printLine():
	print("------------------------------------------------------------------")

def playSong(default = 0):
	global status, sound
	sound = mixer.Sound(soundFiles[fileIndex])
	sound.play(loops=default)
	status = "Now Playing : === '{}' ===".format(soundFiles[fileIndex])

def pauseSong():
	global status, sound
	sound.stop()
	status = 'Paused "{}"'.format(soundFiles[fileIndex])

def nextSong():
	global status, fileIndex, sound
	sound.stop()
	fileIndex += 1
	if fileIndex == len(soundFiles):
		fileIndex = 0
	mixer.init()
	sound = mixer.Sound(soundFiles[fileIndex])
	sound.play()
	status = "Now Playing : === '{}' ===".format(soundFiles[fileIndex])

def prevSong():
	global status, fileIndex, sound
	sound.stop()
	fileIndex -= 1
	if fileIndex < 0:
		fileIndex = len(soundFiles) - 1
	mixer.init()
	sound = mixer.Sound(soundFiles[fileIndex])
	sound.play()
	status = "Now Playing : === '{}' ===".format(soundFiles[fileIndex])

def XthSong():
	global status, fileIndex, sound
	xth = input("Which Number of song would you want to play? (0~{})".format(len(soundFiles) - 1))
	while not xth.isdecimal():
		print("Invalid Choice. Please Choose Again!")
		xth = input("Which Number of song would you want to play? (0~{})".format(len(soundFiles) - 1))
	while int(xth) >= len(soundFiles) or int(xth) < 0: # making sure the length from input doent exceed the amount of music, cuase itll cause an index out of range Error
		print("Invalid Choice. Please Choose Again!")
		xth = input("Which Number of song would you want to play? (0~{})".format(len(soundFiles) - 1))
	sound.stop()
	fileIndex = int(xth)
	mixer.init()
	sound = mixer.Sound(soundFiles[fileIndex])
	sound.play(loops=0)
	status = "Now Playing : === '{}' ===".format(soundFiles[fileIndex])

def main():
	while True:
		menu(status)
		choice = input("Choice: ")
		while choice not in ['0', '1', '2','3','4','5',"7"]:
			print("Invalid Choice! Please Try Again!")
			choice = input("Choice: ")
		printLine()
		if choice == '1':
			playSong()
		elif choice == '2':
			pauseSong()
		elif choice == '3':
			nextSong()
		elif choice == '4':
			prevSong()
		elif choice == '5':
			XthSong()
		elif choice == '0':
			print("Have a nice day! Bye!~")
			break
		else:
			playSong(3) # let it loop~~~ whoohoooo

if __name__ == "__main__":
	fileIndex = 0
	status = ''
	sound = mixer.Sound(soundFiles[fileIndex])
	main()