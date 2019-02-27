from collections import deque
q = deque()

a = input().split()

b = [[0 for i in range(int(a[1]))] for i in range(int(a[0]))]
en = [[False for i in range(int(a[1]))]for i in range(int(a[0]))]
en[0][0] = True
for i in range(int(a[0])):
	c = input()
	for j in range(int(a[1])):
		b[i][j] = int(c[j])
	
q.append([0,0,1])
bfs = []

while len(q) != 0:
	tmp = q.popleft()
	bfs.append(tmp)
	count = tmp[2]
	
	if tmp[1]+1 < int(a[1]):
		if (b[tmp[0]][tmp[1]+1] == 1 and en[tmp[0]][tmp[1]+1] == False):
			q.append([tmp[0],tmp[1]+1,count+1])
			en[tmp[0]][tmp[1]+1] = True
			
	if tmp[0]+1 < int(a[0]):
		if (b[tmp[0]+1][tmp[1]] == 1 and en[tmp[0]+1][tmp[1]] == False):
			q.append([tmp[0]+1,tmp[1],count+1])
			en[tmp[0]+1][tmp[1]] = True
			
	if tmp[1]-1 >= 0:
		if (b[tmp[0]][tmp[1]-1] == 1 and en[tmp[0]][tmp[1]-1] == False):
			q.append([tmp[0],tmp[1]-1,count+1])
			en[tmp[0]][tmp[1]-1] = True
			
	if tmp[0]-1 >= 0:
		if (b[tmp[0]-1][tmp[1]] == 1 and en[tmp[0]-1][tmp[1]] == False):
			q.append([tmp[0]-1,tmp[1],count+1])
			en[tmp[0]-1][tmp[1]] = True
	
min = 0
booleanMin = True
for i in range(len(bfs)):

	if (int(bfs[i][0]+1) == int(a[0]) and int(bfs[i][1]+1) == int(a[1])):
		if booleanMin:
			min = bfs[i][2]
			booleanMin = False
		elif min > bfs[i][2]:
			min = bfs[i][2]
			
print(min)


