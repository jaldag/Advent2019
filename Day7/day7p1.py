def getIntcodeParm(modes, P, ip, parm):
    #Modes:
    # 0 = Value at that address
    # 1 = Value right there
    mode = 0
    try:
        mode = int(modes[-parm])
    except:
        pass
    if mode == 0:
        return P[P[ip + parm]]
    else:
        return P[ip + parm]
def runComputer(phase, val) :
    F = open('input.txt')
    P = [int(x) for x in  F.read().split(',')]
    F.close()

    ip = 0
    inputCount = 0
    while True:
        opcode = int(str(P[ip])[-2:])
        extraOp = str(P[ip])[:-2]
        if opcode == 1 :
            #Add. 1 + 2 into 3's address
            P[P[ip+3]] = getIntcodeParm(extraOp, P, ip, 1) + getIntcodeParm(extraOp, P, ip, 2)
            ip += 4
        elif opcode == 2:
            #Mult. 1 * 2 into 3's address
            P[P[ip+3]] = getIntcodeParm(extraOp, P, ip, 1) * getIntcodeParm(extraOp, P, ip, 2)
            ip += 4
        elif opcode == 3:
            #Get input, put into 1's address
            P[P[ip+1]] = phase if inputCount == 0 else val
            ip += 2
            inputCount += 1
        elif opcode == 4:
            #Print output at 1
            #print "Output: " + str(getIntcodeParm(extraOp, P, ip, 1))
            return getIntcodeParm(extraOp, P, ip, 1)
            ip += 2
        elif opcode == 5 :
            #Jump if True. If value at 1, move pointer to 2's value
            if getIntcodeParm(extraOp, P, ip, 1) > 0 :
                ip = getIntcodeParm(extraOp, P, ip, 2)
            else :
                ip += 3
        elif opcode == 6 :
            #Jump if False. If no value at 1, move point to 2's value
            if getIntcodeParm(extraOp, P, ip, 1) == 0 :
                ip = getIntcodeParm(extraOp, P, ip, 2)
            else :
                ip += 3
        elif opcode == 7 :
            #Less than. if 1 < 2, set 3 to literally 1. Else, set 3 to 0
            if getIntcodeParm(extraOp, P, ip, 1) < getIntcodeParm(extraOp, P, ip, 2) :
                P[P[ip+3]] = 1
            else :
                P[P[ip+3]] = 0
            ip += 4
        elif opcode == 8 :
            #Equals. if 1 == 2, set 3 to literally 1. Else, set 3 to 0
            if getIntcodeParm(extraOp, P, ip, 1) == getIntcodeParm(extraOp, P, ip, 2) :
                P[P[ip+3]] = 1
            else :
                P[P[ip+3]] = 0
            ip += 4
        elif opcode == 99:
            #Exit successfully
            break
        else :
            print "Bad op code: " + str(opcode)
            break

fin = 0
for a in range(0,5) :
    for b in range(0, 5) :
        for c in range(0, 5) :
            for d in range(0, 5) :
                for e in range(0, 5) :
                    if len(set([a, b, c, d, e])) != 5 :
                        continue
                    bIn = runComputer(a, 0)
                    cIn = runComputer(b, bIn)
                    dIn = runComputer(c, cIn)
                    eIn = runComputer(d, dIn)
                    fin = max(runComputer(e, eIn), fin)
print "Part 1: " + str(fin)