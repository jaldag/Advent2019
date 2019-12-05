def opOne(values, op) :
	val1 = values[values[op + 1]]
	val2 = values[values[op + 2]]
	values[values[op + 3]] = val1 + val2
	return values

def opTwo(values, op) :
	val1 = values[values[op + 1]]
	val2 = values[values[op + 2]]
	values[values[op + 3]] = val1 * val2
	return values

file = open("data.txt", "r")
values = file.readline().split(",")

i = 0
while i < len(values) :
	values[i] = int(values[i])
	i = i + 1

op = 0
while values[op] != 99 :
	if values[op] == 1 :
		values = opOne(values, op)
	elif values[op] == 2 :
		values = opTwo(values, op)
	else :
		print "Error: " + str(values[op])
		break
	print values[0]
	if values[0] == 19690720 :
		print str(op)
		break
	op = op + 4

print values