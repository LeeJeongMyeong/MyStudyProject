"""bfs(queue) 를 1개 움직인다
	사람(@)이 움직일 것 하나 
	사람이 먼저 이동하고 불이 이동한다
	불은 번지고 나서 마지막 불의 위치를 바탕으로 좌우 앞뒤를 고려
	"""

from collections import deque
	
def findHuman():
	for i in range(int(a[1])):
		for j in range(int(a[0])):
			if building[i][j] == '@':
				tmp = [i,j]
				return tmp
				
def findFire():
	tmp = []
	for i in range(int(a[1])):
		for j in range(int(a[0])):
			if building[i][j] == '*':
				tmp.append([i,j])
	
	return tmp

def moveHuman(h):
	tmp_count = len(h)
	temp = deque()
	global escape
	global impossible
	
	for i in range(tmp_count):
		x = h[i][0]
		y = h[i][1]
					
		if x == 0 or x == int(a[1]) -1 or y == 0 or y == int(a[0]) -1:
			escape = True
			break
		
		if x > 0 and building[x-1][y] == '.':
			temp.append([x-1, y])
			impossible = True
	
		if x < int(a[1])-1 and building[x+1][y] == '.':
			temp.append([x+1, y])
			impossible = True
		
		if y > 0 and building[x][y-1] == '.':
			temp.append([x, y-1])
			impossible = True
		
		if y < int(a[0])-1 and building[x][y+1] == '.':
			temp.append([x, y+1])
			impossible = True
		
	return temp

		
def moveFire(f):
	count = len(f)
	temp = []
	for i in range(count):
		x = f[i][0]
		y = f[i][1]
		if x > 0 and building[x-1][y] == '.':
			temp.append([x-1, y])
		if x < int(a[1])-1 and building[x+1][y] == '.':
			temp.append([x+1, y])
			
		if y > 0 and building[x][y-1] == '.':
			temp.append([x, y-1])
		
		if y < int(a[0])-1 and building[x][y+1] == '.':
			temp.append([x, y+1])

	return temp

	
answer = []
for i in range(int(input())):
	a = input().split()
	
	building = []
	
	for i in range(int(a[1])):
		building.append(input())
		
	human = deque()
	human.append(findHuman())
	
	fire = findFire()
	count = 1
	
	while human:
		impossible = False
		escape = False
		
		human = moveHuman(human)
		if escape:
			answer.append(count)
			break
		
		if impossible == False:
			answer.append("IMPOSSIBLE")
			break
		
		fire = moveFire(fire)
		
		for i in range(len(fire)):
			tmp = building[fire[i][0]]
			tmp = tmp[:fire[i][1]] + '*' + tmp[fire[i][1]+1:]
			building[fire[i][0]] = tmp

		count += 1
for i in range(len(answer)):
	print(answer[i])
	
"""
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
"""