pic = [x for x in open('input.txt').read()]

width = 25
height = 6
area = width*height

layers = len(pic) / (width * height)

#Part 1
lowLayer = 10000
lowLayerCount = 10000
for layer in range(0, layers) :
	image = pic[layer*area:(layer+1)*area]
	if image.count('0') < lowLayerCount :
		lowLayer = layer
		lowLayerCount = image.count('0')

lowImage = pic[lowLayer*area:(lowLayer+1)*area]
print "Part 1: " + str(lowImage.count('1') * lowImage.count('2'))

#Part 2
finalPic = ['2'] * area
for layer in range(0, layers) :
	for pixel in range(layer*area,(layer+1)*area) :
		if finalPic[pixel % area] == '2' :
			finalPic[pixel % area] = pic[pixel]

print "Part 2:"
print ''.join(finalPic[0:25])
print ''.join(finalPic[25:50])
print ''.join(finalPic[50:75])
print ''.join(finalPic[75:100])
print ''.join(finalPic[100:125])
print ''.join(finalPic[125:150])
print "LEJKC"