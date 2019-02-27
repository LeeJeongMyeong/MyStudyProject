a = int(input())

node = [[0,0] for i in range(a+1)]
first = int(input())
m_count = 0
result = [m_count]

def insert(x, y):
	global m_count 
	global node
	m_count = m_count+1
	if(x<y):
		if node[y][0] == 0:
			node[y][0] = x
		else:
			insert(x, node[y][0])
	else:
		if node[y][1] == 0:
			node[y][1] = x
		else:
			insert(x, node[y][1])

for i in range(a-1):
	tmp = int(input())
	insert(tmp, first)
	result.append(m_count)
	
for i in range(a):
	print (result[i])


	
"""
8
3
5
1
6
8
7
2
4
"""