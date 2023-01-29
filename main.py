"""
The gun beats the snake,,, the water Beats the gun,,,, the snake Beats the water
G > S
W > G
S > W
"""
from colorama import Fore as F
from posMoves import sGW


SGW = ["1","S","SNAKE",
			"2","G","GUN",
			"3","W","WATER"]

printList = ["1 || SNAKE","2 || GUN","3 || WATER"]

print(F.MAGENTA+"\n\t\tSNAKE || WATER || GUN"+F.BLACK+" BY"+F.CYAN+"\n\t\t\t  AHMED-ORACLE"+F.RESET)
print("`"*43)

for option in printList:
	print(option)

userMoves=input(F.YELLOW+"ENTER YOUR MOVES: "+F.RESET).upper().strip()
print("—"*25)
if userMoves in SGW:
	#print(userMoves)
	#print(pickOne())
	sGW(userMoves)
else:
	print(F.RED+"\nYOUR MOVES IS NOT A\nVALID MOVES")
#print("—"*24)

while True:
	print("—"*25)
	print("\nWOULD YOU LIKE TO PLAY AGAIN\nY FOR YES\nN FOR NO")
	playAgain=input("ENTER YOUR CHOICE: ").upper().strip()
	if playAgain=="Y" or playAgain=="YES":
		print("—"*25)
		userMoves = input(F.YELLOW+"\nENTER YOUR MOVES: ").upper().strip()
		if userMoves in SGW:
			sGW(userMoves)
		else:
			print(F.RED+"SAHI WAL DAAL"+F.RESET)
	elif playAgain=="N" or playAgain=="NO":
		print("—"*25)
		print(F.RED+"\nGAME END!!!\nTHANKS FOR PLAYING")
		#score = sGW(None)
		#print (score)
		break
	else: 
		print("—"*25)
		print(F.BLACK+"\nWRONG CHOICE!\nPLEASE ENTER CORRECT CHOICE"+F.RESET)
		