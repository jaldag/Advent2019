P = [x.split(')') for x in open('input.txt').read().splitlines()]

system = {y: x for x, y in P}

#Part 1
count = 0
for node in system :
	index = node
	while index != 'COM' :
		index = system[index]
		count += 1
print count

#Part 2
path = set()
index = system['YOU']
while index != 'COM' :
	path.add(index)
	index = system[index]
index = system['SAN']
while index != 'COM' :
	if index in path :
		path.remove(index)
	else :
		path.add(index)
	index = system[index]
print len(path)