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

def calcPathDistance(wire, index) :
	distance = 0
	for a in range(0, index + 1) :
		distance = distance + int(wire[a][1:])
	return distance

file = open("data.txt", "r")
wire1, wire2 = file.readline().split(","), file.readline().split(",")
points1, points2 = getPoints(wire1), getPoints(wire2)
closest = 10000000
for i in range(0, len(points1) - 1) :
	for j in range(0, len(points2) - 1) :
		if bothPointsCross(points1[i], points1[i+1], points2[j], points2[j+1]) :
			pathDistance = calcPathDistance(wire1, i) + calcPathDistance(wire2, j) + abs(abs(points1[i][0]) - abs(points2[j][0])) + abs(abs(points1[i][1]) - abs(points2[j][1]))
			if pathDistance < closest :
				closest = pathDistance
				print str(points1[i]) + ", " + str(points1[i+1]) + " and " + str(points2[j]) + ", " + str(points2[j+1])
				print "New Closest: " + str(closest)
print closest