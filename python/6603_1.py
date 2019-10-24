def lotto(k, list):
	if k >= len(n):
		return

	list.append(int(n[k]))
	print(k)
	print("--------------------------------------")
	print(list)
	
	if len(list) == 6:
		answer.append(list)
		print("--------------------------------------")
		print(answer)
		for i in range(k+1, z+1):
			list[5] = int(n[i])
			print("--------------------------------------")
			print(list)
			answer.append(list)
			print("--------------------------------------")
			print(answer)
	else:
		lotto(k+1, list)
		for i in range(1, z-6+1):
			k += i
			del(list[len(list)-1])
			lotto(k+i, list)
		

while True:
	n = input().split()
	z = int(n[0])
	answer = []
	tmp = []
	count = 1
	if z == 0:
		break
	elif z == 6:
		for i in range(1, len(n)):
			answer.append(int(n[i]))
		print(answer)
		continue
		
	lotto(count, tmp)

	print(answer)
		
		
		
"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""