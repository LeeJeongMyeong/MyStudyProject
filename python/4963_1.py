import queue

def bfs(y, x):
	global map
	global land_count
	
	que = queue.Queue()
	que.put([x, y])
	
	while que.qsize() > 0:
		tmp = que.get()
		tmp_x = tmp[0]
		tmp_y = tmp[1]
		map[tmp_y][tmp_x] = 0
		
		#x축
		if tmp_x > 0 and int(map[tmp_y][tmp_x-1]) == 1:
			que.put([tmp_x-1, tmp_y])
		if tmp_x < w-1 and int(map[tmp_y][tmp_x+1]) == 1:
			que.put([tmp_x+1, tmp_y])
		#y축
		if tmp_y > 0 and int(map[tmp_y-1][tmp_x]) == 1:
			que.put([tmp_x, tmp_y-1])
		if tmp_y < h-1 and int(map[tmp_y+1][tmp_x]) == 1:
			que.put([tmp_x, tmp_y+1])
		#대각선
		if tmp_x > 0 and tmp_y > 0 and int(map[tmp_y-1][tmp_x-1]) == 1:
			que.put([tmp_x-1, tmp_y-1])
		if tmp_x < w-1 and tmp_y > 0 and int(map[tmp_y-1][tmp_x+1]) == 1:
			que.put([tmp_x+1, tmp_y-1])
		if tmp_x > 0 and tmp_y < h-1 and int(map[tmp_y+1][tmp_x-1]) == 1:
			que.put([tmp_x-1, tmp_y+1])
		if tmp_x < w-1 and tmp_y < h-1 and int(map[tmp_y+1][tmp_x+1]) == 1:
			que.put([tmp_x+1, tmp_y+1])
	
	land_count += 1
	
while True:
	land_count = 0
	map = []
	
	a = input().split()
	w = int(a[0])
	h = int(a[1])
	
	if w == 0 and h == 0:
		break
	
	for i in range(h):
		map.append(input().split())
	
	for i in range(h):
		for j in range(w):
			if int(map[i][j]) == 1:
				bfs(i, j)
	
	print(land_count)
	
"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""