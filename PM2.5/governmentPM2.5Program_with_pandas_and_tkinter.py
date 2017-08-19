# pm2.5 government program with pandas and tkinter for GUI
import pandas as pd
import tkinter as tk
print("getting data ....")
data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
print("daata GET!")

print(data)




def rbCity():
# events for clicking on a city button
	global sitelist, listradio
	sitelist.clear()  # clear original monitor site buttons
	for r in listradio: # clear original monitor buttons
		r.destroy()
	n = 0
	for c1 in data["County"]:
		if c1 == city.get():
			sitelist.append(data.ix[n , 0])
		n += 1
	sitemake() # Build monitor buttons
	rbSite() # show PM2.5 info

def rbSite(): # event function for clicking on monitor buttons
	n = 0
	for s in data.ix[:, 0]: # getting monitor one by one
		if s == site.get(): # getting the clicked monitor
			pm = data.ix[n, "PM2.5"] # getting the PM2.5 values
			if pd.isnull(pm):
				result1.set( s + "Monitor has no data on PM2.5 !")
			else:
				if pm <= 35:  # turn it to levels
					grade1 = "low"
				elif pm <= 53:
					grade1 = "medium"
				elif pm <= 70:
					grade1 = "high"
				else:
					grade1 = "Very High!"
				result1.set(s + "Monitor's PM2.5 value is '" + str(pm) + "' : '" + grade1 + "' level")
			break   # break the loop once monitor is found
		n += 1

def clickRefresh():  # reload data from the internet
	global data
	data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
	rbSite()  # refresh monitor data (as it refreshes every 1 hour on the gorvernment website)

def sitemake():  # build monitor choice buttons
	global sitelist, listradio
	for c1 in sitelist:  # making buttons one by one
		rbtem = tk.Radiobutton(frame2, text=c1, variable=site, value = c1, command=rbSite) # building choice buttons
		listradio.append(rbtem) # add in choice button list
		if c1 ==sitelist[0]:  # set choice is on the first one by default
			rbtem.select()
		rbtem.pack(side="left") # line up on the left side





win = tk.Tk()
win.geometry("640x270")
win.title("PM2.5 InTime Monitor")

city = tk.StringVar() # City's string variables
site = tk.StringVar() #monitor site's variables
result1 = tk.StringVar() # result of monitor variables
citylist = []
sitelist = []
listradio = []

# city list
citylist = [ cit for cit in data["County"] if cit not in citylist] # building the 'unique' city list

print(data)
count = 0
for cit in data["County"]:
	if cit == citylist[0]: # first city's monitor
		sitelist.append(data.ix[count, 0])
	count += 1

label1 = tk.Label(win, text = "City : ", pady = 6, fg = "blue", font = ("Times New Roman", 12))
label1.pack()

frame1 = tk.Frame(win) # cities container
frame1.pack()
#city buttons
for i in range(3):   # 3 lines of buttons container
	for j in range(8): # each line has 8 buttons
		n = i * 8 + j # the nth button
		if n < len(citylist):
			city1 = citylist[n]
			rbtem = tk.Radiobutton(frame1, text = city1, variable = city, value = city1, command = rbCity)
			rbtem.grid(row = i, column = j)  # where buttons go
			if n ==0 :   # the first city will automatically be chosen at the start
				rbtem.select()

label2  = tk.Label(win, text = "Monitor : ", pady = 6, fg = "blue", font = ("Times New Roman", 12))
label2.pack()
frame2 = tk.Frame(win) #monitor container
frame2.pack()

sitemake()

btnDown = tk.Button(win, text= "Refresh Data", font=("Times New Roman", 12), command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(win, textvariable=result1, fg="red", font=("Times New Roman", 16))
lblResult1.pack(pady=6)

rbSite()#shows monitor info

win.mainloop()




	




