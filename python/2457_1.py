n = int(input())

a = []
for i in range(n):
	temp = input().split()
	a.append(temp)
	
search = [3,1]
answer = []

while True:
	tmp = []
	max = [0,0,0,0]

	for i in range(len(a)):
		if int(a[i][0]) <= search[0] and int(a[i][1]) <= search[1]:
			if int(max[2]) < int(a[i][2]):
				max = a[i]
			elif int(max[2]) == int(a[i][2]) and int(max[3]) < int(a[i][3]):
				max = a[i]
		else:
			tmp.append(a[i])
			
	answer.append(max)
	if int(answer[-1][2]) > 11:
		break
	
	search = [int(answer[-1][2]), int(answer[-1][3])]
	a = tmp
	
print(len(answer))

"""
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10
"""