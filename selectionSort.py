## linear iteration find the minimum
## swap minimum with previous minimum value
## start from the next value, find the minimum
## swap with the previous 
import datetime
from random import randint

timer_start = datetime.datetime.now()

sortMeArray = []
for i in range(0,100):
	sortMeArray.append(randint(0,1000))
# print sortMeArray



def selectionSort(sortMe):
	for x in range(len(sortMe)):
		minimum = x
		# maximum = 0
		# print minimum
		for y in range(x+1,len(sortMe)):
			# print y
			if sortMe[y] < sortMe[minimum]:
				minimum = y
				
		# temp = sortMe[x]
		# sortMe[x] = sortMe[minimum]
		# sortMe[minimum] = temp
		sortMe[x], sortMe[minimum] = sortMe[minimum], sortMe[x]

	return sortMe

sortedArray = selectionSort(sortMeArray)
print sortedArray


## The below needs work
def modifiedSelectionSort(sortMe):
	for x in range(len(sortMe)):
		minimum = x
		maximum = x
		for y in range(x+1,len(sortMe)):
			if sortMe[y] < sortMe[minimum]:
				minimum = y
			if sortMe[y] > sortMe[maximum]:
				maximum = y
			print "the Min index is "+str(minimum)
			print "the Max index  is "+str(maximum)
		sortMe[x], sortMe[minimum] = sortMe[maximum], sortMe[x]
		
	
	
	return sortMe

# sortedArray = selectionSort(sortMeArray)
modSortedArray = modifiedSelectionSort(sortMeArray)
# print sortedArray
print modSortedArray

timer_end = datetime.datetime.now()
totalTime = timer_end - timer_start
print totalTime