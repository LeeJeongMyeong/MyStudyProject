n = int(input())

rgb = []

for i in range(n):
	rgb.append(input().split())
	
minR = 0
minG = 0
minB = 0

resultR = int(rgb[0][0])
color = 0
for i in range(n-1):
	if color == 0:
		resultR += min(int(rgb[i+1][1]), int(rgb[i+1][2]))
		if int(rgb[i+1][1]) < int(rgb[i+1][2]):
			color = 1
		else:
			color = 2
		continue
		
	if color == 1:
		resultR += min(int(rgb[i+1][0]), int(rgb[i+1][2]))
		if int(rgb[i+1][0]) < int(rgb[i+1][2]):
			color = 0
		else :
			color = 2
		continue
		
	if color == 2:
		resultR += min(int(rgb[i+1][0]), int(rgb[i+1][1]))
		if int(rgb[i+1][0]) < int(rgb[i+1][1]):
			color = 0
		else :
			color = 1
		continue
			
resultG = int(rgb[0][1])
color = 1
for i in range(n-1):
	if color == 0:
		resultG += min(int(rgb[i+1][1]), int(rgb[i+1][2]))
		if int(rgb[i+1][1]) < int(rgb[i+1][2]):
			color = 1
		else:
			color = 2
		continue
		
	if color == 1:
		resultG += min(int(rgb[i+1][0]), int(rgb[i+1][2]))
		if int(rgb[i+1][0]) < int(rgb[i+1][2]):
			color = 0
		else :
			color = 2
		continue
		
	if color == 2:
		resultG += min(int(rgb[i+1][0]), int(rgb[i+1][1]))
		if int(rgb[i+1][0]) < int(rgb[i+1][1]):
			color = 0
		else :
			color = 1
		continue

resultB = int(rgb[0][2])
color = 2
for i in range(n-1):
	if color == 0:
		resultB += min(int(rgb[i+1][1]), int(rgb[i+1][2]))
		if int(rgb[i+1][1]) < int(rgb[i+1][2]):
			color = 1
		else:
			color = 2
		continue
		
	if color == 1:
		resultB += min(int(rgb[i+1][0]), int(rgb[i+1][2]))
		if int(rgb[i+1][0]) < int(rgb[i+1][2]):
			color = 0
		else :
			color = 2
		continue
		
	if color == 2:
		resultB += min(int(rgb[i+1][0]), int(rgb[i+1][1]))
		if int(rgb[i+1][0]) < int(rgb[i+1][1]):
			color = 0
		else :
			color = 1
		continue

print (min(resultR, resultG, resultB))
"""
3
26 40 83
49 60 57
13 89 99
96

"""