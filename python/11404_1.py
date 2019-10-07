#플로이드 와샬

a = int(input())

cost = [[100000 for i in range(a)]for i in range(a)]

for i in range(a):
	cost[i][i] = 0

for i in range(int(input())):
	tmp = input().split()
	tmp_x = int(tmp[0]) - 1
	tmp_y = int(tmp[1]) - 1
	tmp_cost = int(tmp[2])
	if cost[tmp_x][tmp_y] > tmp_cost:
		cost[tmp_x][tmp_y] = tmp_cost
		
#중간지점
for i in range(a):
	#시작점
	for j in range(a):
		#도착지점
		for k in range(a):
			tmp = cost[j][i] + cost[i][k]
			if cost[j][k] > tmp:
				cost[j][k] = tmp
for i in range(a):
	tmp = "" + str(cost[i][0])
	for j in range(a-1):
		tmp = tmp + " " + str(cost[i][j+1])
	print(tmp)


"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""