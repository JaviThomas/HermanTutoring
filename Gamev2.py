import random
from getpass import getpass



def gameSelectionTwoPlayer():
	print("Player 1, what do you choose? Don't show player two!")

	def validateChoice(selection):
		if selection == "rock":
			pass
		elif selection == "paper":
			pass
		elif selection == "scissors":
			pass
		else:
			selection = input("that didn't look right. Please try again.\n")
			validateChoice(selection)

	player_1 = getpass("rock, paper, scissors\n")
	validateChoice(player_1)
	player_2 = getpass("Player 2, now its your turn, what do you choose? \nrock, paper, scissors\n")
	validateChoice(player_2)

	# computer has options 0,1,2

	if player_1 == "rock":
		if player_2 == "rock":
			restartAfterPlay("one_tie")
		elif player_2 == "paper":
			restartAfterPlay("one_loss")
		else:
			restartAfterPlay("one_win")

	if player_1 == "paper":
		if player_2 == "rock":
			restartAfterPlay("one_win")
		elif player_2 == "paper":
			restartAfterPlay("one_tie")
		else:
			restartAfterPlay("one_loss")

	if player_1 == "scissors":
		if player_2 == "rock":
			restartAfterPlay("one_loss")
		elif player_2 == "paper":
			restartAfterPlay("one_win")
		else:
			restartAfterPlay("one_tie")


def gameStart():
	print("Welcome to the Game." + "Are you ready to play?")
	user = input("yes/no\n")
	if user == "yes":
		decision = input("Do you want to play [1] player/ [2] player?\n")
		gameMode(decision)
	else:
		print("Too Bad")
	return decision


def gameMode(decision):

	if decision == '1':
		print("Let's see what you got!")
		gameSelectionOnePlayer()
	elif decision == '2':
		print("Ok, lets start it up! Good luck to you both!!")
		gameSelectionTwoPlayer()
	else:
		decision = input("Sorry, Did you want to play [1] player/ [2] player?\n")
		gameMode(decision)



def gameSelectionOnePlayer():

	print("which do you choose?")
	#which do you pick? rock, paper, scissors

	userSelection = input("rock, paper, scissors\n")
	if userSelection == "rock":
		pass
	elif userSelection == "paper":
		pass
	elif userSelection == "scissors":
		pass
	else:
		userSelection = input("that didn't look right. Please try again.\n")

	#computer has options 0,1,2

	masterKey = {0: "rock", 1: "paper", 2: "scissors"}
	computerSelection = masterKey[random.randint(0, 2)]

	print("computer has chosen " + computerSelection)

	if userSelection == "rock":
		if computerSelection == "rock":
			restartAfterPlay("User_tie")
		elif computerSelection == "paper":
			restartAfterPlay("User_loss")
		else:
			restartAfterPlay("User_win")

	if userSelection == "paper":
		if computerSelection == "rock":
			restartAfterPlay("User_win")
		elif computerSelection == "paper":
			restartAfterPlay("User_tie")
		else:
			restartAfterPlay("User_loss")

	if userSelection == "scissors":
		if computerSelection == "rock":
			restartAfterPlay("User_loss")
		elif computerSelection == "paper":
			restartAfterPlay("User_win")
		else:
			restartAfterPlay("User_tie")


def restartAfterPlay(result):
	names = {
		"User_win": "Congratulations you win!!!",
		'User_tie': "Nobody wins ;(",
		"User_loss": "you lose too bad xD",
		'one_win': "Congrats player 1, you win!",
		'one_tie': "looks like you both think the same, its a tie!",
		'one_loss': "Congrats player 2, you win!"
	}
	playAgain = input(names[result] + "\nPlay one player [1] \nPlay two player [2] \nExit![0]\n")

	if not (playAgain == 0 or 1 or 2):
		playAgain = input("Please retype selection, 0,1 or 2")

	if playAgain == "0":
		print("Bye bye!")
		exit()
	elif playAgain == "1":
		print("begin 1 player")
		gameSelectionOnePlayer()
	elif playAgain == "2":
		print("begin 2 player")
		gameSelectionTwoPlayer()


#random. rock, paper, scissors

#if computer chooses rock and I chose scissors

#computer wins
