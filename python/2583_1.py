import queue

def bfs(y, x):
	q = queue.Queue()
	q.queue.clear()
	q.put([y,x])
	t_count = 0
	visit[y][x] = 1
	while not q.empty():
		t_count += 1
		tmp = q.get()
		tmp_y = int(tmp[0])
		tmp_x = int(tmp[1])
		
		if tmp_x > 0 and visit[tmp_y][tmp_x-1] == 0:
			q.put([tmp_y, tmp_x-1])
			visit[tmp_y][tmp_x-1] = 1
			
		if tmp_x < max_x-1 and visit[tmp_y][tmp_x+1] == 0:
			q.put([tmp_y, tmp_x+1])
			visit[tmp_y][tmp_x+1] = 1
			
		if tmp_y > 0 and visit[tmp_y-1][tmp_x] == 0:
			q.put([tmp_y-1, tmp_x])
			visit[tmp_y-1][tmp_x] = 1
			
		if tmp_y < max_y-1 and visit[tmp_y+1][tmp_x] == 0:
			q.put([tmp_y+1, tmp_x])
			visit[tmp_y+1][tmp_x] = 1
			
	land_count.append(t_count)


t = input().split()
max_y = int(t[0])
max_x = int(t[1])
block = int(t[2])

visit = [[0 for i in range(int(t[1]))]for i in range(int(t[0]))]
count = 0
land_count = []

for i in range(block):
	tmp = input().split()
	for j in range(int(tmp[0]), int(tmp[2])):
		for k in range(int(tmp[1]), int(tmp[3])):
			visit[k][j] = 1

for i in range(max_y):
	for j in range(max_x):
		if visit[i][j] == 0:
			bfs(i, j)
			count += 1
print(count)
land_count.sort()
for i in range(len(land_count)):
	print(land_count[i], end = ' ')

"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""
"""answer
3
1 7 13
"""
"""
0 1 0 0 0 0 0
1 1 1 1 0 0 0
1 1 1 1 0 0 0
0 1 0 0 1 1 0
0 0 0 0 1 1 0
"""