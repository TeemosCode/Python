# -*- encoding = 'UTF-8' -*-
# getting rid of zip
# written by the coolest dude on earth: teemo!


"""
This program is the classic hangman game played on the termianl. 
How to play:  The first person enters a word for others to guess, the words would then be hidden with "_" unless they are correctly
guessed, thats when those correctly guessed characters will show. Each player that tries to get the word will have 6 chances to guess
what character the answer contains by guessing a character for each chance. Once 6 chances are used and the player did not get the 
correct answer, he would be considered hanged and lost the game, otherwise, he/she would be victorious.
"""

# The function that takes in player's guessed character input, and does changes to the answer and life of the player
#  according to the input of the players.
def match_character(inpt: str):
	"""
	The function takes in the user's guessed characer input and checks to see if the character exists in the answer, and performs actions
	regarding whether the guessed character is in the answer or not.

	:params inpt: A single character input typed in by the user
	:return : Boolean. If the user got all characters correct before health runs out, it returns True. Else, return false. Used for breaking the game loop.
	"""
	# Add the guessed character into the guessed_words set to prevent users from replicating guesses.
	global guessed
	global health

	guessed_words.add(inpt)

	if inpt not in answer:
		print("'{}' does not exist in the anser, you lost 1 health\n".format(inpt))
		# player loses one health if guessed character is not in the ans
		health -= 1
	else:
		# calls function when the input character belongs in answer
		print("Nice guess! '{}' exists in the anser\n".format(inpt))
		if word_matched(inpt):
			return True
	return False

def word_matched(inpt: str):
	"""
	This function handles the current guessed status of the answer, changing its hiddent value to the character that users correctly guessed.
	Also, it checks if the user got all the characters right or not to match the answer.

	:params inpt: A single character input typed in by the user.
	:return : Boolean. If the user got all characters correct before health runs out, it returns True. Else, return false. Used for breaking the game loop.
	"""
	# loop through answer to find the indexs where the user's guessed character is.
	global answer
	global status


	for index in range(len(answer)):
		if answer[index] == inpt:
			# change the list index character value that matches the index where the user's guessed character is in the answer from '_' to the character itself for outputting
			status[index] = inpt 

	if ''.join(status) == answer:
		print("\n\nCongratulations!! You got the answer '{}' correct!!\n\n".format(answer) )
		return True
	return False


def show_status():
	"""
	This function prints out the current game status of the player
	"""
	global health
	global guessed_words
	global status

	print(
		"""Current Status:
		   Health: {},
		   Guessed words: {},

		   Current Word Status: {}

		""".format(health, guessed_words, ''.join(status)))

def game_start():
	"""
	This function initializes the values and data structures at the start of each game once a player types in the to-be-guessed word
	for others to guess for futher usage.
	"""
	# The answer variable that saves input from the first user for other players to guess. It is altered to lower case.
	global answer
	global status

	print("Game Started. Hello Ruler, please think of a word to rule the others!\n")
	answer = input("Input a word for others to guess:  ")
	while " " in answer or type(answer) != str:
		print("The input could only contain ONE WORD! Please try again!")
		answer = input("Input ONE word for others to guess:  ")

	answer.lower() # change the answer to lower case.
	
	print("Ruler has entered the word that will rule all. Please guess the word ONE CHARACTER at a time for each chance you have!\n You only have 6 chances, please use it wisely!\n\n")
	# The status list that will be displayed each round through the join() method and would update its output everytime a user guessed
	# a character that belongs in the answer string.
	status = ["_" for i in range(len(answer))] 

	print("Current Health : {}".format(health))

def main():
	"""
	The main function of the game, it takes users (players) characters inputs then calls other functions to preform logic process on the input
	"""
	global victory
	game_start()

	while health != 0:
		user_guess = input("Enter one Character for guessing:  ")
		while len(user_guess) != 1 or user_guess in guessed_words:
			if user_guess in guessed_words:
				print("The character '{}' has already been guessed, please guess a new character\n".format(user_guess))
			else:
				print("Invalid input!! Please enter ONE CHARACTER for guessing!\n")
			user_guess = input("Enter one Character for guessing:  ")

		user_guess.lower() # change it to lower case

		if match_character(user_guess): # check to see if the guessed character belongs in answer
			victory = 1
			break

		show_status() # shows the current game status
	if victory:
		print("VICTORIOUS! Congratulations, you are the WINNER, you are now the new RULER of this world!\n")
	else:
		print("GAME OVER! Your health ran our! You got HANGED!")


if __name__ == "__main__":
	# initialize the global game variables
	answer = '' # initialize the answer as an empty string, it will be changed once game_start function is called.
	health = 6
	guessed_words = set() # A set containing the characters guessed by the players
	status = list() # The status list that will be displayed each round through the join() method to show current guessed status
	victory = 0 # variable for checking if player is victorious or not. Used for jumping to the correct corresponding ending message.

	while True:

		main()

		print("Would you like to start the game again?")
		restart = input("Please enter 'Y' or 'y' to continue. (Press any other keys to exit.)")
		# If user enters anything other than 'Y' or 'y', the game exits
		if restart == 'Y' or restart == 'y':
			# reinitialize the values for a new round
			health = 6
			guessed_words = set() # A set containing the characters guessed by the players
			status = list() # The status list that will be displayed each round through the join() method to show current guessed status
			victory = 0 # variable for checking if player is victorious or not. Used for jumping to the correct corresponding ending message.
		else:
			print("\nGood Bye! Have a nice day!")
			break







# def match_up(inpt):
#     a = '_' * len(inpt)
#     print("Try guessing this word: " + a + "\n lET'S PLAY A GAME, u have 6 Chances yolo")
#     l = list(a)
#     words = []
#     hp = 6
#     lala = []
#     while hp != 0:
#         print('\nHP remaining:\n%d'% hp)
#         if (''.join(l)) == server_input:
#             restart= input("Yo ****!! You got it right! Congratulations! You survived for another day!!\nAnswer: %s\nWanna keep hanging?(Y/y):" % ("".join(l)) )
#             restart = restart.lower()
# #fixed --- 2017/7/31
#             if restart == 'y':
#                 return True
#             else:
#                 print("Good bye ****!!!")
#                 lala.append("FLAG")
#                 return False
            
            
#         client_guess = input('Enter the character for guessing, choose carefully~! \n:')
        

#         if len(client_guess) != 1:
#             print("Please don't be blind, you can guess only ONE character !!!!\n What u have now:" , (''.join(l)) )


#         elif client_guess not in server_input :
#             if client_guess in words:
#                 print('Geeze~! I ALREADY told u u *****!! its not in the answer !\n What u have now:' , (''.join(l))  )
#             else:
#                 words.append(client_guess)
#                 hp -= 1
#                 print('word NOT in answer! Lost 1 HP, you\'re dying~!\n What u have now:' , (''.join(l)) )
#         elif client_guess in server_input:
#             if client_guess in words:
#                 print('You\'ve already guessed this once, please guess another new one, don\'t wana get urself killed eh?!!\n What u have now:' , (''.join(l)) )
#             else:
#                 print('\'%s\' in answer, NICE GUESS!!!'% client_guess)            
#                 words.append(client_guess)
#                 i = 0
#                 for c in server_input:
#                     if c == client_guess:
#                         l[i] = client_guess
#                         i += 1
#                         print('The answer now looks like this : \n%s' % (''.join(l)) )
#                     else:
#                         i+= 1
#     if len(lala) > 0 :
#         pass
#     else:
#         print('\nHP remaining:\n%d'% hp)
#         print('*****! lost all the HP,u dead man. You got HANGED!')
#         restart = input("Good Try though!\nWanna keep hanging?(Y/y):"  )
#         restart.lower()
#         if restart == 'y':
#             match_up(server_input)
#         else:
#             print("Bye~")
#             return False



# if __name__ == '__main__':
#     server_input = input('Enter a word for Guessing!\n:')
#     while server_input != 'TeemoHasDied666':
#         keepgoing = match_up(server_input)
#         if not keepgoing:
#             print("Bye~!!")
#             break
#         else:
#             server_input = input('Enter a word for Guessing!\n:')
        
