######## Chapter 6 ########
####     Flip Coin     ####
import random
import time

print(''' I will flip coins for 100 times.
Guess how many times heads will come up. 
\ (Press Enter to begin)''')
input()
flips = 0 
heads = 0 
while flips < 1000:
	if random.randint(0,1) == 1:
		heads += 1 
	flips += 1
	
	if flips == 900:
		print(" 900 flips and there has been "+ str(heads) + " heads.")
		time.sleep(2)
	if flips == 100:
		print(" 100 flips and there has been "+ str(heads) + " heads.")
		time.sleep(2)
	if flips == 500:
		print(" Half way down! And the heads has come up "+ str(heads) + " times.")
		time.sleep(2)

print()
print(" Out of 100 coin tosses, head came up "+ str(heads) + "times! ")
print(" Were you close ?")
