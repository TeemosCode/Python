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







	




