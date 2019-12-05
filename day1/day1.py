import math

def calculate(value) :
	if value >= 9 :
		new = math.floor(value / 3) - 2
		if calculate(int(new)) >= 0 and int(new) >= 0:
			return int(new) + calculate(int(new))
		else :
			return int(new)
	else :
		return 0

file = open("data.txt", "r")

values = []

for x in file :
	values.append(int(x))

fuel = []

for value in values :
	fuel.append(calculate(value))

total = 0
for val in fuel :
	total = total + val

print total