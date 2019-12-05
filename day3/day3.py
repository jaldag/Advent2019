def getPoints(wire) :
	points = []
	x = 0
	y = 0
	for val in wire :
		if val[:1] == 'R' :
			x = x + int(val[1:])
		elif val[:1] == 'L' :
			x = x - int(val[1:])
		elif val[:1] == 'U' :
			y = y + int(val[1:])
		elif val[:1] == 'D' :
			y = y - int(val[1:])
		points.append([x, y])
	return points

def pointsCross(x1, x2, x3, x4) :
	return x1 < x3 and x2 > x4 or x1 > x3 and x2 < x4

def bothPointsCross(point1, point2, point3, point4) :
	return pointsCross(point1[0], point2[0], point3[0], point4[0]) and pointsCross(point1[1], point2[1], point3[1], point4[1])

file = open("data.txt", "r")
points1, points2 = getPoints(file.readline().split(",")), getPoints(file.readline().split(","))
closest = 1000000
for i in range(0, len(points1) - 1) :
	for j in range(0, len(points2) - 1) :
		if bothPointsCross(points1[i], points1[i+1], points2[j], points2[j+1]) :
			if points1[i][0] == points1[i+1][0] :
				distance = abs(points1[i][0])
			elif points1[i][1] == points1[i+1][1] :
				distance = abs(points1[i][1])
			if points2[j][0] == points2[j+1][0] :
				distance = distance + abs(points2[j][0])
			elif points2[j][1] == points2[j+1][1] :
				distance = distance + abs(points2[j][1])
			if distance < closest :
				closest = distance
				print str(points1[i]) + ", " + str(points1[i+1]) + " and " + str(points2[j]) + ", " + str(points2[j+1])
				print "New Closest: " + str(closest)
print closest