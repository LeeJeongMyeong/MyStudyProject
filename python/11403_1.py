import queue

n = int(input())
a = []
for i in range(n):
	a.append(input().split())
	
#BFS
visit = [[0 for i in range(n)]for i in range(n)]
q = queue.Queue()

for i in range(n):
	q.queue.clear()
	for j in range(n):
		if int(a[i][j]) == 1:
			q.put(j)
	
	while not q.empty():
		tmp = q.get()
		visit[i][tmp] = 1
		for j in range(n):
			if int(a[tmp][j]) == 1 and visit[i][j] == 0:
				q.put(j)
	
	for j in range(n):
		print(visit[i][j], end=' ')
	print()

"""
3
0 1 0
0 0 1
1 0 0

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
"""
"""answer
1 1 1
1 1 1
1 1 1

1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
"""