a = input().split()

v = int(a[0])
e = int(a[1])

inf = 100000000

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

for i in range(v):
	cost[start][i] = [cost[start][i], False]

tmp_start = start
while True:
	lastCost = cost[start][tmp_start][0]
	cost[start][tmp_start][1] = True
	
	for i in range(v):
		if cost[start][i][0] > cost[tmp_start][i]+lastCost:
			cost[start][i] = [cost[tmp_start][i]+lastCost, False]
	
	minimum = []
	for i in range(v):
		if cost[start][i][1]:
			continue
			
		if not minimum:
			minimum = [i, cost[start][i][0]]
		elif minimum[0] > cost[start][i][0]: 
				minimum = [i, cost[start][i][0]]
				
	if not minimum:
		break
		
	tmp_start = minimum[0]
	
for i in range(v):
	if cost[start][i][0] == inf:
		print("INF")
	else:
		print(answer[i][0])

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