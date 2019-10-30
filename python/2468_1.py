import queue
import copy

def bfs():
	global answer
	t_visit = copy.deepcopy(visit)
	q = queue.Queue()
	q.queue.clear()
	count = 0
	for i in range(n):
		for j in range(n):
			if t_visit[i][j] == 0:
				count += 1
				q.put([i,j])
				t_visit[i][j] = 1
				while not q.empty():
					tmp = q.get()
					tmp_x = tmp[0]
					tmp_y = tmp[1]

					if tmp_x > 0 and t_visit[tmp_x-1][tmp_y] == 0:
						q.put([tmp_x-1, tmp_y])
						t_visit[tmp_x-1][tmp_y] = 1

					if tmp_x < n-1 and t_visit[tmp_x+1][tmp_y] == 0:
						q.put([tmp_x+1, tmp_y])
						t_visit[tmp_x+1][tmp_y] = 1

					if tmp_y > 0 and t_visit[tmp_x][tmp_y-1] == 0:
						q.put([tmp_x, tmp_y-1])
						t_visit[tmp_x][tmp_y-1] = 1

					if tmp_y < n-1 and t_visit[tmp_x][tmp_y+1] == 0:
						q.put([tmp_x, tmp_y+1])
						t_visit[tmp_x][tmp_y+1] = 1
	if answer < count:
		answer = count

n = int(input())
area = []
answer = 1
for i in range(n):
	area.append(input().split())
	for j in range(n):
		area[i][j] = int(area[i][j])

visit = [[0 for i in range(n)] for i in range(n)]

for i in range(1,101):
	checker = False
	first = []
	for j in range(n):
		for k in range(n):
			if area[j][k] == i:
				checker = True
				visit[j][k] = 1
	if checker:
		bfs()

print(answer)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""
"""answer
5
"""