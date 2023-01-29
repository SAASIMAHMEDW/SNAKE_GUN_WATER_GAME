"""
The gun beats the snake,,, the water Beats the gun,,,, the snake Beats the water
G > S
W > G
S > W

all pos
S S  S G  S W
G G  G S  G W
W W  W G  W S

"""
from comChoice import pickOne
from colorama import Fore as F


def sGW(userChoice):
	userScore = 0
	computerScore = 0
	tieScore = 0
	comChoice = pickOne()
	print(F.CYAN + f"\nYOUR MOVES IS: {userChoice}")
	print(f"COM MOVES IS: {comChoice}")
	print(F.MAGENTA)
	if userChoice == comChoice:
		print("TIE!!!")
		tieScore += 1

	elif userChoice == "SNAKE" and comChoice == "GUN":
		print("GUN WIN!!!")
		print("COM WON THE GAME")
		computerScore += 1

	elif userChoice == "SNAKE" and comChoice == "WATER":
		print("SNAKE WIN!!!")
		print("USER WON THE GAME")
		userScore += 1

	elif userChoice == "GUN" and comChoice == "SNAKE":
		print("GUN WIN!!!")
		print("USER WON THE GAME")
		userScore += 1

	elif userChoice == "GUN" and comChoice == "WATER":
		print("WATER WIN!!!")
		print("COM WON THE GAME")
		computerScore += 1

	elif userChoice == "WATER" and comChoice == "GUN":
		print("WATER WIN!!!")
		print("USER WON THE GAME")
		userScore += 1

	elif userChoice == "WATER" and comChoice == "SNAKE":
		print("SNAKE WIN!!!")
		print("COM WON THE GAME")
		computerScore += 1
	print(F.RESET)

	# print("TOTAL USER WINS: ",userScore)
	# print("TOTAL COM WINS: ",computerScore)
	# print("TOTAL TIES: ",tieScore)
	#return userScore, computerScore, tieScore


if __name__ == "__main__":
	userMoves = input("ENTER YOUR MOVES: ").upper().strip()
	sGW(userMoves)
