def drawStars(stars):
	for x in range(len(stars)):
		print ""
		if type(stars[x]) is str:
			# print stars[x]
			for i in range(len(stars[x])):
				print str.lower(stars[x][0]),
		else:
		# now for each item we want to print that number of stars
			for y in range(0,stars[x]):
				print "*",

myStarsList = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

drawStars(myStarsList)
