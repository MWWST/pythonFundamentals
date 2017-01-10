import datetime
from random import randint

timer_start = datetime.datetime.now()

sortMeArray = []
for i in range(0,100):
	sortMeArray.append(randint(0,1000))
# print sortMeArray

def recursiveSelectionSort(arry,startIndex):
	if startIndex > len(arry):
		return arry
	minIndex = startIndex
	for x in range(startIndex+1,len(arry)):
		if arry[x] < arry[minIndex]:
			minIndex = x
		temp = arry[x]
		arry[x] = arry[minIndex]
		arry[minIndex] = temp
		# arry[x], arry[startIndex] = arry[minIndex], arry[x]
	recursiveSelectionSort(arry, startIndex + 1)

recrisvelySorted = recursiveSelectionSort(sortMeArray,0)
print recrisvelySorted