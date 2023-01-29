
def pickOne():
	choices = ["SNAKE",
		   "GUN",
		   "WATER"]
	import random
	#print (choices)
	random.shuffle(choices)
	#print(choices)
	com = random.choice(choices)
	#print(com)
	return com

if __name__ == "__main__":
	x = pickOne()
	print (x)
