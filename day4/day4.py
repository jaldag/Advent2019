legal = []
legal2 = []

for y in [str(x) for x in range(136760, 595730)] :
	if y == ''.join(sorted(y)) :
		for digit in y :
			if y.count(digit) >= 2 :
				legal.append(y)
				break
print "Part 1: " + str(len(legal))

for z in legal :
	for digit in z :
		if z.count(digit) == 2 :
			legal2.append(z)
			break
print "Part 2: " + str(len(legal2))