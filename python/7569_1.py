import queue

def bfs():
	l = q.qsize()
	for i in range(l):
		tmp = q.get()
		t_m = tmp[0]
		t_n = tmp[1]
		t_h = tmp[2]
	
		if t_m > 0 and tomato[t_h][t_n][t_m-1] == 0:
			q.put([t_m-1, t_n, t_h])
			tomato[t_h][t_n][t_m-1] = 1
		if t_m < m-1 and tomato[t_h][t_n][t_m+1] == 0:
			q.put([t_m+1, t_n, t_h])
			tomato[t_h][t_n][t_m+1] = 1
			
		if t_n > 0 and tomato[t_h][t_n-1][t_m] == 0:
			q.put([t_m, t_n-1, t_h])
			tomato[t_h][t_n-1][t_m] = 1
		if t_n < n-1 and tomato[t_h][t_n+1][t_m] == 0:
			q.put([t_m, t_n+1, t_h])
			tomato[t_h][t_n+1][t_m] = 1
		
		if t_h > 0 and tomato[t_h-1][t_n][t_m] == 0:
			q.put([t_m, t_n, t_h-1])
			tomato[t_h-1][t_n][t_m] = 1
		if t_h < h-1 and tomato[t_h+1][t_n][t_m] == 0:
			q.put([t_m, t_n, t_h+1])
			tomato[t_h+1][t_n][t_m] = 1
			

m, n, h = map(int, input().split())
tomato = [[[] for i in range(n)]for i in range(h)]
day = 0
q = queue.Queue()
q.queue.clear()
checker = True

for i in range(h):
	for j in range(n):
		tomato[i][j] = input().split()
		
		for k in range(m):
			tomato[i][j][k] = int(tomato[i][j][k])
			if tomato[i][j][k] == 1:
				q.put([k, j, i])
			
			if checker and tomato[i][j][k] == 0:
				checker = False

if checker:
	print(day)
else:
	while not q.empty():
		day += 1
		bfs()

	check = True
	for i in range(h):
		for j in range(n):
			for k in range(m):
				if tomato[i][j][k] == 0:
					check = False
					break
			if not check:
				break
		if not check:
			break

	if check:
		print(day-1)
	else:
		print(-1)
	
	
	
	
	
"""
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

3 3 2
1 0 1
0 0 0
1 0 1
0 0 0
0 1 0
0 0 0

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
"""
"""answer
-1

4

1

0
"""