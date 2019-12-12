from copy import deepcopy
from itertools import count

def calcGravity(moonsPos, moon1, moon2, axis) :
	return 1 if moonsPos[moon1][axis] < moonsPos[moon2][axis] else (-1 if moonsPos[moon1][axis] > moonsPos[moon2][axis] else 0)

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

#moonsPos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
moonsPos = [[16, -11, 2], [0, -4, 7], [6, 4, -10], [-3, -2, -4]]

initPos = deepcopy(moonsPos)

moonsVel = [[0] * 3 for _ in range(4)]

initVel = deepcopy(moonsVel)

cycles = [None, None, None]

for step in count(start=1) :
	for moon1 in range(len(moonsPos)) :
		for moon2 in range(0, len(moonsPos)) :
			moonsVel[moon1][0] += calcGravity(moonsPos, moon1, moon2, 0)
			moonsVel[moon1][1] += calcGravity(moonsPos, moon1, moon2, 1)
			moonsVel[moon1][2] += calcGravity(moonsPos, moon1, moon2, 2)
	for moon in range(len(moonsPos)) :
		moonsPos[moon][0] += moonsVel[moon][0]
		moonsPos[moon][1] += moonsVel[moon][1]
		moonsPos[moon][2] += moonsVel[moon][2]

	if step == 1000 :
		energy = 0
		for idx in range(len(moonsPos)) :
			energy += ((abs(moonsPos[idx][0]) + abs(moonsPos[idx][1]) + abs(moonsPos[idx][2])) * (abs(moonsVel[idx][0]) + abs(moonsVel[idx][1]) + abs(moonsVel[idx][2])))
		print "Part 1: " + str(energy)

	for cycle in range(3) :
		if cycles[cycle] == None :
			for moon in range(len(moonsPos)) :
				if moonsPos[moon][cycle] != initPos[moon][cycle] :
					break
				if moonsVel[moon][cycle] != initVel[moon][cycle] :
					break
			else :
				cycles[cycle] = step
	if all(cycles) :
		print "Part 2: " + str(lcm(cycles[0], lcm(cycles[1], cycles[2])))
		break