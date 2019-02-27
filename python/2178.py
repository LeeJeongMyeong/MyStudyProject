import queue
from collections import deque
q = queue.Queue()

a = input().split()

b = [[0 for i in range(int(a[1]))] for i in range(int(a[0]))]
en = [[False for i in range(int(a[1]))]for i in range(int(a[0]))]
#print(en)
for i in range(int(a[0])):
	c = input()
	for j in range(int(a[1])):
		b[i][j] = int(c[j])
	
#print(b)
q.put([0,0])

bfs = []
print(a[0],a[1])

while q.qsize() != 0:
	tmp = q.get()
	#print(tmp)
	bfs.append(tmp)
	en[tmp[0]][tmp[1]] = True

	if tmp[1]+1 < int(a[1]):
		if (b[tmp[0]][tmp[1]+1] == 1 and en[tmp[0]][tmp[1]+1] == False):
			q.put([tmp[0],tmp[1]+1])
			
	if tmp[0]+1 < int(a[0]):
		if (b[tmp[0]+1][tmp[1]] == 1 and en[tmp[0]+1][tmp[1]] == False):
			q.put([tmp[0]+1,tmp[1]])
			
	if (tmp[0]+1 < int(a[0]) and tmp[1] + 1 < int(a[1])):
		if (b[tmp[0]+1][tmp[1]+1] == 1 and en[tmp[0]+1][tmp[1]+1] == False):
			q.put([tmp[0]+1,tmp[1]+1])
			
	print(int(q.qsize))

"""
	if tmp[1]-1 > 0:
		if (b[tmp[0]][tmp[1]-1] == 1 and en[tmp[0]][tmp[1]-1] == False):
			q.put([tmp[0],tmp[1]-1])
			
	if tmp[0]-1 > 0:
		if (b[tmp[0]-1][tmp[1]] == 1 and en[tmp[0]-1][tmp[1]] == False):
			q.put([tmp[0]-1,tmp[1]])
			
	if (tmp[0]-1 > 0 and tmp[1]-1 > 0):
		if (b[tmp[0]-1][tmp[1]-1] == 1 and en[tmp[0]-1][tmp[1]-1] == False):
			q.put([tmp[0]-1,tmp[1]-1])
	"""
print(bfs)