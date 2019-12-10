import math

space = [x for x in open('input.txt').read().replace('\n', '')]
length = len(open('input.txt').readline().replace('\n', ''))
num = maxCount = maxX = maxY = 0
for val in space :
	x = num % length
	y = int(num / length)
	if val == '#' :
		count = 0
		see = set()
		num2 = 0
		for val2 in space :
			if val2 == '#' and num != num2 :
				see.add(math.atan2(int(num2 / length) - y, num2 % length - x))
			num2 += 1
		if len(see) > maxCount :
			maxCount = len(see)
			maxX = x
			maxY = y
	num += 1
print "Part 1: " + str(maxX) + ", " + str(maxY) + " Length: " + str(maxCount)

slopeDict = {}
num2 = 0
for val2 in space :
	if val2 == '#' and num2 != (maxY * length + maxX) :
		val = math.atan2(int(num2 / length) - maxY, num2 % length - maxX)
		try :
			slopeDict[val].append([num2 % length, int(num2 / length)])
		except :
			slopeDict[val] = [[num2 % length, int(num2 / length)]]
	num2 += 1
keys = sorted(slopeDict.keys())

firstIndex = count = 0
for key in keys :
	if key >= math.atan2(-1, 0) :
		firstIndex = keys.index(key)
		break
twoHundredth = [0, 0]
while True :
	for key in keys[firstIndex:] :
		if slopeDict[key] != None and slopeDict != []:
			closest = [10000, 10000]
			for val in slopeDict[key] :
				if abs(maxX - val[0]) <= abs(closest[0] - val[0]) and abs(maxY - val[1]) <= abs(closest[1] - val[1]) :
					closest = val
			if closest != [10000, 10000] :
				slopeDict[key].remove(closest)
				count += 1
				if count == 200 :
					twoHundredth = closest
					break
	firstIndex = 0
	if count == 200 :
		break
print twoHundredth