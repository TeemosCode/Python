#little ppl know of this smaller plotting library in python. it does not take up as much space and memory as matplotlib (like 1/5 the amount)
#mostly used for much lesser fnacy stuff ~~
# Another significant difference is that bokeh uses web browsers to open up the images
from bokeh.plotting import figure, show, output_file

f = figure(width= 800, height=600, title="Savings Recodrds")
f.title_text_color = "green"
f.title_text_font_size = "20pt"

f.xaxis.axis_label="Age"
f.xaxis.axis_label_text_color = "violet"
f.yaxis.axis_label="Savings"
f.yaxis.axis_label_text_color ="violet"

dashs = [12,4]

listx1 = [1,5,7,9,13,16]
listy1 = [15,59,80,40,70,50]

f.line(listx1, listy1, line_width=4, line_color="red", line_alpha = 0.3, line_dash=dashs, legend="Male")

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
f.line(listx2, listy2, line_width=4, legend="Female")

show(f)

print('--------------------')
input('--------Press Enter to Proceed with the next cool stuff, Wink**--------------')

f = figure(width=800, height=600, title = "Savings Record")
output_file("SavingsBokeh.html") #changing the title of the picture, cause default sets it to the same name as the python file
f.title_text_font_size = "32pt"
f.title_text_color = "blue"
f.xaxis.axis_label = "X"
f.yaxis.axis_label = "Y"

sizes = [45,25,30,50,40,60]

colors = ['red','blue','green','violet','gray','pink']
#sizes = 50 # to set all points as a fixed size	
#colors = "blue" #set all colors to a fixed blue
f.circle(listx1, listy1, size=sizes, color=colors, alpha=0.5)
show(f)
print("===============There Are Many More Kinds To Look At===============\n\n")



def showMenu():
	print(
		"""
		=======================
		-----------------------
		|1. circle_x          |
		|2. square_cross      |
		|3. inverted_triangle |
		|4. asterisk           |
		|5. x                 |
		|6. circle_cross      |
		|7. square            |
		|8. square_x          |
		|9. triangle          |
		|10. cross            |
		-----------------------
		=======================
		""")

def difBokehStyle(choice):
	f = figure(width=800, height=600, title = "Savings Record")
	if choice == "1":
		f.circle_x(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '2':
		f.square_cross(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '3':
		f.inverted_triangle(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '4':
		f.asterisk(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '5':
		f.x(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '6':
		f.circle_cross(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '7':
		f.square(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '8':
		f.square(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '9':
		f.triangle(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	elif choice == '10':
		f.cross(listx1, listy1, size=sizes, color=colors, alpha=0.5)
	show(f)

def main():
	while True:
		showMenu()
		choice = input("Please Choose one of the above numbers (1 ~ 10) to see the visual differences [Press Enter without typing anything to QUIT]")
		if choice == '':
			print('-----\nGOODBYE!\n-----')
			break
		while choice not in ["1",'2','3','4','5','6','7','8','9','10']:
			print("Do not have the choice of {} ! Pleas follow the instruction,\
			 or You can either be stuck doing this or just destroy your computer!".format(choice))
			choice = input("Please Choose one of the above numbers (1 ~ 10) to see the visual differences [Press Enter without typing anything to QUIT]")
			if choice == '':
				break
		if choice == '':
			print('-----\nGOODBYE!\n-----')
			break

		difBokehStyle(choice)

main()