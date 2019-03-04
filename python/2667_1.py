a = int(input())

b = [[0 for i in range(a)] for i in range(a)]

enable = [[True for i in range(a)]for i in range(a)]
answer = []
count = 0

def dfs(x, y):
	enable[x][y] = False
	if (x > 0 and b[x-1][y] == 1 and enable[x-1][y]):
		answer[count-1] += 1
		dfs(x-1,y)
		
	if (y > 0 and b[x][y-1] == 1 and enable[x][y-1]):
		answer[count-1] += 1
		dfs(x, y-1)
			
	if (x + 1 < a and b[x+1][y] == 1 and enable[x+1][y]):
		answer[count-1] += 1
		dfs(x+1, y)
		
	if (y + 1 < a and b[x][y+1] == 1 and enable[x][y+1]):
		answer[count-1] += 1
		dfs(x, y+1)
			
for i in range(a):
	c = input()
	for j in range(len(c)):
		b[i][j] = int(c[j])


for i in range(a):
	for j in range(a):
		if(enable[i][j] and b[i][j] == 1):
			answer.append(1)
			count += 1
			dfs(i, j)
		
print(count)
answer.sort()
for i in range(len(answer)):
	print(answer[i])




"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
"""