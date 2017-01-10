# iterate through the array
# check if the next number is smaller than the current number
# 	if it is smaller then we need to swap the two numbers
#
import datetime
from random import randint

timer_start = datetime.datetime.now()

listToSort = []
for i in range(0,100):
	listToSort.append(randint(0,1000))

def insertionSort(sortThis):
	for index in range(1,len(sortThis)):
		value = sortThis[index]

		left = index - 1
		while left >=0:
			if value < sortThis[left]:
				sortThis[left+1] = sortThis[left] # to the right
				sortThis[left] = value # to the left
				left = left - 1
			else:
				break
	return sortThis

sortedArray = insertionSort(listToSort)
print sortedArray
timer_end = datetime.datetime.now()
totalTime = timer_end - timer_start
print totalTime