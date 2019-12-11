from collections import defaultdict

def getIntcodeParm(modes, P, ip, parm, rBase, location = False):
    #Modes:
    # 0 = Value at that address
    # 1 = Value right there
    mode = 0
    try:
        mode = int(modes[-parm])
    except:
        pass
    if mode == 0:
        return P[P[ip + parm]] if not location else P[ip + parm]
    elif mode == 1:
        return P[ip + parm] if not location else ip + parm
    elif mode == 2:
        return P[P[ip + parm] + rBase] if not location else P[ip + parm] + rBase

def runComputer(part2 = False) :
    F = open('input.txt')
    P = [int(x) for x in  F.read().split(',')] + [0] * 1000000
    F.close()
    rBase = 0
    ip = 0

    directionIndex = outputMutex = x = y = 0
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] #Up, Right, Down, Left
    spaceMap = defaultdict(int)
    if part2 :
    	spaceMap[(0, 0)] = 1

    ipAdd = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
    while True:
        opcode = int(str(P[ip])[-2:])
        extraOp = str(P[ip])[:-2]
        if opcode == 1 :
            #Add. 1 + 2 into 3's address
            P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = getIntcodeParm(extraOp, P, ip, 1, rBase) + getIntcodeParm(extraOp, P, ip, 2, rBase)
            ip += ipAdd[opcode]
        elif opcode == 2:
            #Mult. 1 * 2 into 3's address
            P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = getIntcodeParm(extraOp, P, ip, 1, rBase) * getIntcodeParm(extraOp, P, ip, 2, rBase)
            ip += ipAdd[opcode]
        elif opcode == 3:
            #Get input, put into 1's address
            P[getIntcodeParm(extraOp, P, ip, 1, rBase, True)] = spaceMap[(x, y)]
            ip += ipAdd[opcode]
        elif opcode == 4:
            #Print output at 1
        	v = getIntcodeParm(extraOp, P, ip, 1, rBase)
        	if outputMutex % 2 == 0 :
           		spaceMap[(x, y)] = v
        	else :
           		if v == 1 :
           			directionIndex += 1
           		elif v == 0 :
           			directionIndex += -1
           		x += direction[directionIndex % 4][0]
           		y += direction[directionIndex % 4][1]
        	outputMutex += 1
        	ip += ipAdd[opcode]
        elif opcode == 5 :
            #Jump if True. If value at 1, move pointer to 2's value
            if getIntcodeParm(extraOp, P, ip, 1, rBase) > 0 :
                ip = getIntcodeParm(extraOp, P, ip, 2, rBase)
            else :
                ip += ipAdd[opcode]
        elif opcode == 6 :
            #Jump if False. If no value at 1, move point to 2's value
            if getIntcodeParm(extraOp, P, ip, 1, rBase) == 0 :
                ip = getIntcodeParm(extraOp, P, ip, 2, rBase)
            else :
                ip += ipAdd[opcode]
        elif opcode == 7 :
            #Less than. if 1 < 2, set 3 to literally 1. Else, set 3 to 0
            if getIntcodeParm(extraOp, P, ip, 1, rBase) < getIntcodeParm(extraOp, P, ip, 2, rBase) :
                P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = 1
            else :
                P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = 0
            ip += ipAdd[opcode]
        elif opcode == 8 :
            #Equals. if 1 == 2, set 3 to literally 1. Else, set 3 to 0
            if getIntcodeParm(extraOp, P, ip, 1, rBase) == getIntcodeParm(extraOp, P, ip, 2, rBase) :
                P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = 1
            else :
                P[getIntcodeParm(extraOp, P, ip, 3, rBase, True)] = 0
            ip += ipAdd[opcode]
        elif opcode == 9 :
            # Change Relative Base
            rBase += getIntcodeParm(extraOp, P, ip, 1, rBase)
            ip += ipAdd[opcode]
        elif opcode == 99:
            #Exit successfully
            break
        else :
            print "Bad op code: " + str(opcode)
            break
    return spaceMap

spaceMap = runComputer()
print "Part 1: " + str(len(spaceMap.keys()))

spaceMap = runComputer(True)
print "Part 2: "
for x in range(0, 42) :
	line = ''
	for y in range(-15, 20) :
		if spaceMap[(x, y)] == 1 :
			line = line + 'X'
		else :
			line = line + ' '
	print line