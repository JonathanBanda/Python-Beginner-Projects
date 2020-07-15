from tkinter import *
import random

"""
WE ARE GOING TO CREATE A ROCK PAPER SCISSORS GAME TERMINAL GAME

"""

# The scoreboard counter
your_ScoreBoard = 0
computer_ScoreBoard = 0

# all the game options

game_Options = {
	'rock' : 1,
	'paper' : 2,
	'scissors' : 3,
	'exit' : 0
}

print("Welcome to Rock, Paper, Scissors\n")
print("The following are your options.\n")

for key, value in game_Options.items():
	print(key)

option = input("\nPlease select an option: ").lower()

#main loop

while game_Options.get("exit") == 0:

	if option == "exit":
		break

	computer_Choice = random.randint(1, 3)

	if computer_Choice == 1 and game_Options.get(option) == 1:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 0
		print("Tie \nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 1 and game_Options.get(option) == 2:
		your_ScoreBoard+= 1
		computer_ScoreBoard+= 0
		print("Point for You\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 1 and game_Options.get(option) == 3:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 1
		print("Point for Computer\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	if computer_Choice == 2 and game_Options.get(option) == 1:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 1
		print("Point for Computer\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 2 and game_Options.get(option) == 2:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 0
		print("Tie \nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 2 and game_Options.get(option) == 3:
		your_ScoreBoard+= 1
		computer_ScoreBoard+= 0
		print("Point for You\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	if computer_Choice == 3 and game_Options.get(option) == 1:
		your_ScoreBoard+= 1
		computer_ScoreBoard+= 0
		print("Point for You\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 3 and game_Options.get(option) == 2:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 1
		print("Point for Computer\nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)

	elif computer_Choice == 3 and game_Options.get(option) == 3:
		your_ScoreBoard+= 0
		computer_ScoreBoard+= 0
		print("Tie \nScoreboard: [You vs Comp.]", your_ScoreBoard, computer_ScoreBoard)


	if your_ScoreBoard == 3 or computer_ScoreBoard == 3:
		break

	option = input("\nPlease select an option: ").lower()



















