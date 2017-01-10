myList = []

for x in range(0,10):
	print "What is your score?"
	thisEntry = input()
	myList.insert(x,thisEntry)

for x in range(len(myList)):
	if myList[x] <59:
		grade = "F"
	elif myList[x] >=60 and myList[x] <=69:
		grade = "D"
	elif myList[x] >=70 and myList[x] <=79:
		grade = "C"
	elif myList [x] >=80 and myList[x] <= 89:
		grade = "B"
	else:
		grade = "A"
	print "Score is", str(myList[x]) + '; Your grade is ' + grade