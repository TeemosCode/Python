from firebase import firebase
import time


url = "https://pythonchineseenglishdictionary.firebaseio.com/"
app = '/EnglishChineseDictionary'
fb = firebase.FirebaseApplication(url + app, None) # you can insert full path, which is the parent of all
# or relative path, for certain other urls

'''

#basic applications and functions
fb.post(app, "Python") #inserts data "Python" into the url database, random generates an id for this data
dic = fb.post(app, "Yolo") # this WILL STILL update the firbase
print(dic["name"]) # the "name" built-in key outputs the UNIQUE id. here its : -KpU72zEv8MGVltSsmSA
# Also with each time we process the program, itll keep adding it in, it wont check if the Values of the data already exists or not
'''
#data in dictionary style
#fb.post(app, {"roger":4})
'''
data = fb.get(app,None)
for key in data:
	print(data[key])
'''
'''
fb.delete(app +"/" + "-KpU6pv8z5N53opSUAM5", None) # the '/' is important lol
fb.put(app, data={"roger":100}, name = "UniqueID_var_is_name)")
'''


#in this dictionary firebase program, the unique "name" id is gona be the english vocabulary itself
def menu():
	print(
	"""
	===== Welcome to your own Chinese & English Firebase Dictionary =====
	  (Choose the numbers for choices of acion to do with the database)
		   --------------------------------------------------------

				   1. Query Vocabulary
				   2. Save New Vocabulary
				   3. Show Vocabulary
				   4. Delete Vocabulary
				   5. Update Vocabulary
				   0. END Program

		   ---------------------------------------------------------


	""")

def printLine():
	print('---------------------------------------------------------')

def dataExists(name):
	global data
	if name in data:
		return True
	else:
		return False

def QueryVocabulary():
	"""
	Prints out 20 lines of vocabulary each time
	"""
	global data
	counter = 0
	while True:
		printLine()
		eVoc = input("Enter the English Vocabulary (Pressing Enter without any inputs QUITS the action): ")
		if eVoc == '':
			printLine()
			print("Bye")
			break
		if dataExists(eVoc):
			counter += 1
			print(str(counter) + ". " + data[eVoc])
		else:
			print("Vocabulary '{}' can not be found!".format(eVoc))



def SaveVocabulary():
	global data
	while True:
		printLine()
		eVoc = input("Enter the English vocabulary to be saved (Pressing Enter without any inputs QUITS the action): ")
		if eVoc == '':
			printLine()
			print("bye")
			break
		cVoc = input("Enter its Chinese meaning: ")
		while cVoc == '':
			print("Cannot input meaningless string, please try again, it's for your own good!")
			cVoc = input("Enter its Chinese meaning: ")
		newVoc = fb.put(app, data = cVoc, name = eVoc)
		# keep the data on the database on the cloud and in this program synced
		data[eVoc] = cVoc
		print("New vocabularies, '{} : {}' ... Saved!".format(eVoc, cVoc))
		printLine()

def ShowVocabulary():
	global data
	counter = 0
	
	while True:
		printLine()
		print("Vocabularies (print 20 lines each time, press Enter wihtout input to continue, or press 'q' to stop)")
		printLine()
		n, line = 0, 20
		data_keys = sorted(data.keys())
		for eVoc in data_keys:
			n += 1
			counter += 1
			print("%10d" % counter + ". " + eVoc + " : " + data[eVoc])

			if n == line:
				printLine()
				cont = input("what to do")
				while cont != "" and cont!= "q":
					cont = input(" what to do")
				if cont == "q":
					return None
				else:
					n = 0
					printLine()
		break #Displayed all data, break the loop or we're gona keep seeing the same stuff over and over till all eternity. well of course if the batteries never run out, if so, this computer is gona be a savier of human energy yooooo!!!!




def DeleteVocabulary():
	global data
	while True:
		printLine()
		eVoc = input("Enter the Vocabulary to Delete (Pressing Enter without any inputs QUITS the action): ")
		if eVoc == "":
			printLine()
			print("Bye")
			break
		if dataExists(eVoc):
			check = input("Are you sure you want to delete the Vocabulary: '{}' and its Chinese Meaning: '{}'? [y/n]".format(eVoc, data[eVoc]))
			while check.lower() != 'n' and check.lower() != 'y':
				print("Invalid Choice, please try again!")
				check = input("Are you sure you want to delete the Vocabulary: '{}' and its Chinese Meaning: '{}'? [y/n]".format(eVoc, data[eVoc]))
			if check.lower() == "y":
				fb.delete(app + '/' + eVoc, None)
				
				print("Vocabulary '{}' and its Chinese meaning '{}' DELETED!".format(eVoc, data[eVoc]))
				#keep it sync
				del data[eVoc]
			else:
				print("Deletion Denied!")
		else:
			print("Vocabulary: '{}' Does NOT exist!".format(eVoc))


def UpdateVocabulary():
	global data
	while True:
		printLine()
		eVoc = input("Enter the english word you want to update (Pressing Enter without any inputs QUITS the action): ")
		if eVoc == "":
			printLine()
			print("Bye")
			break
		if dataExists(eVoc):
			print("English\tChinese\n'{}'\t'{}'".format(eVoc, data[eVoc]))
			cVoc = input("Enter its NEW Chinese meaning: ")
			while cVoc == '':
				print("Cannot input meaningless string, please try again, it's for your own good!")
				cVoc = input("Enter its Chinese meaning: ")
			fb.put(app, data = cVoc, name = eVoc)
			#keep it sync
			data[eVoc] = cVoc
			print("Vocabularies, '{} : {}' ... Updated!".format(eVoc, cVoc))
		else:
			print("Vocabulary '{}' can not be found! Please Try again!".format(eVoc))


def main():
	while True:
		menu()
		choice = input("Enter your choice of action: ")
		while choice not in ['1','2','3','4','5','0']:
			print("Invalid Choice. Please Try Again!")
			choice = input("Enter your choice of action: ")

		if choice == '1':
			QueryVocabulary()
		elif choice == '2':
			SaveVocabulary()
		elif choice == '3':
			ShowVocabulary()
		elif choice == '4':
			DeleteVocabulary()
		elif choice == '5':
			UpdateVocabulary()
		elif choice == "0":
			print("GoodBye. Exiting Firebase Dictionary Program...")
			printLine()
			break

if __name__ == "__main__":

	data = fb.get(app, None)
	main()


