## linear iteration find the minimum
## swap minimum with previous minimum value
## start from the next value, find the minimum
## swap with the previous 

from random import randint
sortMeArray = []
for i in range(0,100):
	sortMeArray.append(randint(0,1000))


def selectionSort(sortMe):
	for x in range(len(sortMe)):
		minimum = x
		print minimum
		for y in range(x+1,len(sortMe)):
			# print y
			if sortMe[y] < sortMe[minimum]:
				minimum = y
				
		temp = sortMe[x]
		sortMe[x] = sortMe[minimum]
		sortMe[minimum] = temp
	return sortMe

sortedArray = selectionSort(sortMeArray)
print sortedArray