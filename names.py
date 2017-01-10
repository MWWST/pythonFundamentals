studentsArray = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def combineNames(students):
	for x in range(len(students)):
		for attr, value in students[x].iteritems():
			print value,
		print "\n"

# combineNames(studentsArray)


def instructorStudents(object):
	students = 0
	instructors = 0
	for key, data in users.items():
		print key
 		for value in data:
 			if key == "Students":
 				students += 1
 				print students, value["first_name"], value[
 				"last_name"]
 				# print value
 			else:
 				instructors +=1
 				print instructors, value["first_name"], value["last_name"]
 				# print value 
 			# print data

instructorStudents(users)