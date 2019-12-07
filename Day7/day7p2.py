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
def runComputer() :
    F = open('input.txt')
    P = [int(x) for x in  F.read().split(',')]
    F.close()

    ip = 0
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
            P[P[ip+1]] = yield
            ip += 2
        elif opcode == 4:
            #Print output at 1
            yield getIntcodeParm(extraOp, P, ip, 1)
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
            raise StopIteration()
        else :
            print "Bad op code: " + str(opcode)
            raise StopIteration()

fin = 0
for a in range(5,10) :
    for b in range(5, 10) :
        for c in range(5, 10) :
            for d in range(5, 10) :
                for e in range(5, 10) :
                    if len(set([a, b, c, d, e])) != 5 :
                        continue
                    aComp = runComputer()
                    next(aComp); aComp.send(a)
                    bComp = runComputer()
                    next(bComp); bComp.send(b)
                    cComp = runComputer()
                    next(cComp); cComp.send(c)
                    dComp = runComputer()
                    next(dComp); dComp.send(d)
                    eComp = runComputer()
                    next(eComp); eComp.send(e)

                    val = 0
                    end = 0
                    for lo in range(100000000) :
                        done = False
                        for comp in (aComp, bComp, cComp, dComp, eComp) :
                            try :
                                if lo != 0 :
                                    next(comp)
                                val = comp.send(val)
                                if comp == eComp :
                                    end = val
                            except StopIteration:
                                done = True
                                break;
                        if done :
                            break
                    fin = max(end, fin)
                    #Print it going so I know the damn thing isn't in infinite loop
                    print fin
print "Part 2: " + str(fin)