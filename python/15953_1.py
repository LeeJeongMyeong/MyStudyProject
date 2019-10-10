t = int(input())

for i in range(t):
	tmp = input().split()

	a = int(tmp[0])
	b = int(tmp[1])
	
	money = 0
	if a == 0:
		money += 0
	elif a == 1:
		money += 5000000
	elif a > 1 and a <= 3:
		money += 3000000
	elif a > 3 and a <= 6:
		money += 2000000
	elif a > 6 and a <= 10:
		money += 500000
	elif a > 10 and a <= 15:
		money += 300000
	elif a > 15 and a <= 21:
		money += 100000
	else:
		money += 0
		
	if b == 0:
		money += 0
	elif b == 1:
		money += 5120000
	elif b > 1 and b <= 3:
		money += 2560000
	elif b > 3 and b <= 7:
		money += 1280000
	elif b > 7 and b <= 15:
		money += 640000
	elif b > 15 and b <= 31:
		money += 320000
	else:
		money += 0
		
	print(money)
	
"""
6
8 4
13 19
8 10
18 18
8 25
13 16
"""