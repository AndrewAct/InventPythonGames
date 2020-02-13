######## Chapter 5 ########
####    Dragon Realm   ####
import random
import time

def displayIntro():
	print('''You are in a land full of dragons. 
	In front of you, there are two caves.
	In one cave, the dragons are fiendly 
	and will share his treasure with you.
	In another, the dragons are hundry and greedy,
	and will eat you on sight. ''')
print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print("Which cave will you go into? (1 or 2)")
		cave = input()
		
	return(cave)
	
def checkCave():
	print(" You are approaching the cave. ")
	time.sleep(2)
	print(" It is dark and spooky. ")
	time.sleep(2)
	print("A dragon is in front of you! He opens his mouth and ...")
	print()
	time.sleep(2)
	friendlyCave = random.randint(1,2)
	if chooseCave == str(friendlyCave):
		print(" Gives you his treasure !")
	else:
		print(" Gobbles you down in one bite !")
		
playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
	displayIntro()
	caveNumber = chooseCave()
	checkCave()
	
	print(" Do you want to play again? (yes or no)")
	playAgain = input()