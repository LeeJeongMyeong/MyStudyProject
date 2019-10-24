import copy
def lotto(x, y):
	if x >= c:
		return
	
	tmp = copy.deepcopy(y)
	tmp.append(b[x])
	nextNum = x+1
	
	if len(tmp) == 6:
		answer.append(tmp)
		for i in range(nextNum, c):
			z = copy.deepcopy(y)
			z.append(b[i])
			answer.append(z)
	else:
		lotto(nextNum, tmp)
		z = copy.deepcopy(y)
		for i in range(nextNum, c):
			lotto(i, z)

while True:
	a = input().split()
	c = int(a[0])
	if c == 0:
		break
	elif c == 6:
		tmp = []
		for i in range(c):
			tmp.append(int(a[i+1]))
		print(tmp)
		continue

	answer = []
	b = a[1:]
	for i in range(c):
		b[i] = int(b[i])

	lotto(0, [])
	print(answer)


"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""

""" answer
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
"""