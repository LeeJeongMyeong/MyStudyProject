a = input()
b = []
while True:
	c = input().split()
	b.append(c)
	if c[1] == a:
		break

#DFS
st = [[0,1,0]]
max = [0,0]
size = len(b)
c = []
while st:
	tmp = st.pop()
	found = tmp[1]
	flag = True
	count = []
	for i in range(len(b)):
		if int(b[i][0]) == found:
			st.append([int(b[i][0]), int(b[i][1]), int(b[i][2]) + tmp[2]])
			count.append(i)
			flag = False

	count.sort(reverse = True)
	for i in range(len(count)):
		c.append(b.pop(count[i]))
		
	if flag:
		if max[1] < tmp[2]:
			max[1] = tmp[2]
			max[0] = tmp[1]

			
b = b+c
st = [[0, max[0], 0]]
visit = [False for i in range(size)]
max = [0, 0]

while st:
	tmp = st.pop()
	found  = tmp[1]
	flag = True
	count = []
	for i in range(len(b)):
		if int(b[i][0]) == found:# and visit[i] == False:
			st.append([int(b[i][0]), int(b[i][1]), int(b[i][2]) + tmp[2]])
			flag = False
			#visit[i] = True
			count.append(i)

		elif int(b[i][1]) == found:# and visit[i] == False:
			st.append([int(b[i][1]), int(b[i][0]), int(b[i][2]) + tmp[2]])
			flag = False
			#visit[i] = True
			count.append(i)
	
	count.sort(reverse = True)
	for i in range(len(count)):
		b.pop(count[i])
	
	if flag:
		if max[1] < tmp[2]:
			max[1] = tmp[2]
			max[0] = tmp[1]

print (max[1])	


"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
"""