import random
heads = 0
tails = 0

#Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 

print "Starting program..."
for x in range(0,5000):
	randomNum = random.random()
	print randomNum
	finalNum = round(randomNum)
	print finalNum
	if finalNum == 0:
		current = "head"
		heads += 1
		print "Attempt #" + str(x) + ": Throwing a coin... It's a"+ current+ " Got "+ str(heads) +" head(s) so far and " + str(tails) + " tail(s) so far"
	else:
		current = "tail"
		tails +=1
		print "Attempt #" + str(x) + ": Throwing a coin... It's a"+ current+ " Got "+ str(heads) +" head(s) so far and " + str(tails) + " tail(s) so far"
print "Ending the program... Thank You"