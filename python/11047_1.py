tmp = input().split()

n = int(tmp[0])
k = int(tmp[1])
coin = []
for i in range(n):
	coin.append(int(input()))

count = 0

for i in range(n):
	if k <= 0:
		break
	a = n-i-1
	
	if k >= coin[a]:
		count += k//coin[a]
		k = k%coin[a]
		
#	while k >= coin[a]:
#		k -= coin[a]
#		count += 1
print(count)

"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""