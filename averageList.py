a = [1, 2, 5, 10, 255, 3]
total = 0

for x in range(0,len(a)):
	#print a[x]
	total += a[x]
average = total / len(a)
print average 