P = [x.split(')') for x in open('input.txt').read().splitlines()]

class Node:
	def __init__(self, name) :
		self.name = name
		self.down = []
		self.up = []

def countNodeOrbits(node, nodeCount) :
	if len(node.down) == 0 :
		return nodeCount
	totalCount = 0
	for orbit in node.down :
		totalCount += countNodeOrbits(orbit, nodeCount + 1)
	return totalCount

def findSAN(node, nodeCount, already) :
	if node.name in already :
		return 10000
	if node.name == 'SAN' :
		return nodeCount
	totalCount = 10000
	already.append(node.name)
	for orbit in node.up + node.down :
		totalCount = min(totalCount, findSAN(orbit, nodeCount + 1, list(already)))
	return totalCount

nodes = {}
for x in P :
	if not (x[0] in nodes.keys()) :
		nodes[x[0]] = Node(x[0])
	if not (x[1] in nodes.keys()) :
		nodes[x[1]] = Node(x[1])
	nodes[x[1]].down.append(nodes[x[0]])
	nodes[x[0]].up.append(nodes[x[1]])

#Part 1
count = 0
for node in nodes :
	count += countNodeOrbits(nodes[node], 0)
print "Part 1: " + str(count)

#Part 2
print "Part 2: " + str(findSAN(nodes['YOU'], 0, []) - 2)