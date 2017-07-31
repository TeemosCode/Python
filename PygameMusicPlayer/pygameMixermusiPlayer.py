# usage of the pygame mixer 'music' attribute --> which can play long media files llike .mp3 files
import tkinter as tk
from pygame import mixer
import glob

mixer.init()

#musid file paths for future use
sourceDir = "mp3/"

mp3Files = glob.glob(sourceDir + "*.mp3")
mp3Files = [ files.split("mp3/")[1] for files in mp3Files ] #getting rid of the 'mp3/' strings at the front of every file, looks disgusting

#setting up tkinter GUI window
window = tk.Tk()
window.geometry("1024x800")
window.title("MP3 Player")

labelTitle = tk.Label(window, text="\nMP3 Player", fg = "blue", font = ("Times New Roman", 50))
labelTitle.pack()

frame1 = tk.Frame(window)
frame1.pack()
print(mp3Files) #checking whether the music file paths are working or not
playSong = prePlaySong = mp3Files[0] # used for loading songs with mixer.music and the displaying name

index = 0 # which song we on
volume = 0.6
choice = tk.StringVar()  # the check box of choosing songs, returning song strings for futher usage


def choose():
	global playSong
	msg.set("\nNow Playing\n ===" + choice.get() + "===")
	playSong = choice.get() #tkinter method usage for getting the string of the choice

def pauseMp3():
	mixer.music.pause()
	msg.set("\nPaused '{}'".format(prePlaySong))

def increase():
	global volume
	volume += 0.1
	if volume >= 1:
		volume=1
	mixer.music.set_volume(volume)

def decrease():
	global volume
	volume -= 0.1
	if volume <= 0.3:
		volume=0.3
	mixer.music.set_volume(volume)

#!
def playMp3():
	global status, playSong, prePlaySong
	if playSong == prePlaySong:
		if not mixer.music.get_busy():
			mixer.music.load('mp3/' + playSong)
			mixer.music.play(loops=-1)
		else:
			mixer.music.unpause()
		msg.set("\nNow Playing\n ==={}".format(playSong) + "===")
	else:
		playNewMp3() #!
		prePlaySong=playSong

def playNewMp3():
	global playSong
	mixer.music.stop() #STOP THE previous song
	mixer.music.load('mp3/' + playSong) # load the different song to play
	mixer.music.play(loops=-1)# play it
	msg.set("\nNow Playing\n ==={}".format(playSong) + '===')

def stopMp3():
	mixer.music.stop()
	msg.set("MP3 Player STOPPED")

def quit():
	mixer.music.stop()
	window.destroy()


# creating choices music name fill in thingys
for mp3 in mp3Files: 
	rbtem = tk.Radiobutton(frame1, text=mp3, variable=choice, value=mp3, command=choose)
	if index == 0:
		rbtem.select()
		playSong = prePlaySong = mp3
	rbtem.grid(row=index, column=0, sticky='w')
	index += 1

msg = tk.StringVar() # important! used for setting all messages on the GUI
msg.set("\nChoose a Song to Play")

label = tk.Label(window, textvariable=msg, fg= "red", font=("Times New Roman", 30))
label.pack()

labelSep = tk.Label(window, text='\n')
labelSep.pack()

frame2 = tk.Frame(window)
frame2.pack()
button1 = tk.Button(frame2, text="Play", width=8, command=playMp3)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(frame2, text="Pause", width=8, command=pauseMp3)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(frame2, text="Increase Vol", width=8, command=increase)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(frame2, text="Decrease Vol", width=8, command=decrease)
button4.grid(row=0, column=3, padx=5, pady=5)
button5 = tk.Button(frame2, text="Stop", width=8, command=stopMp3)
button5.grid(row=0, column=4, padx=5, pady=5)
button6 = tk.Button(frame2, text="Quit", width=8, command=quit)
button6.grid(row=0, column=5, padx=5, pady=5)
window.protocol("WM_DELETE_WINDOW", quit) # the "X" on the window
window.mainloop()



