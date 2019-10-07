def getSmallIndex():
	min = inf
	index = 0
	global distance
	for i in range(v):
		if check[i] == False and distance[i] < min:
			min = distance[i]
			index = i
			
	return index
	
def dijkstra(started):
	for i in range(v):
		distance[i] = cost[started][i]
	check[started] = True
	
	for i in range(v-2):
		current = getSmallIndex()
		check[current] = True
		
		for j in range(v):
			if check[j] == False:
				if distance[current] + cost[current][j] < distance[j]:
					distance[j] = distance[current] + cost[current][j]
			

inf = 100000000
a = input().split()
v = int(a[0])
e = int(a[1])

cost = [[inf for i in range(v)]for i in range(v)]

for i in range(v):
	cost[i][i] = 0

start = int(input())-1

for i in range(e):
	tmp = input().split()
	tmp_x = int(tmp[0]) - 1
	tmp_y = int(tmp[1]) - 1
	tmp_cost = int(tmp[2])
	cost[tmp_x][tmp_y] = tmp_cost

check = [False for i in range(v)]
distance = [inf for i in range(v)]

dijkstra(start)
for i in range(v):
	if distance[i] == inf:
		print("INF")
	else:
		print(distance[i])


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""