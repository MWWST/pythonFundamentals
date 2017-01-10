def myMultiplier(list,multipler):
	for x in range(len(list)):
		list[x] *= multipler
	return list

myArray = [2,4,10,16]

b = myMultiplier(myArray,5)
print b