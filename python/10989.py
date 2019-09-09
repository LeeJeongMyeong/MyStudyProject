a = int(input())

b = []

for i in range(a):
	b.append(int(input()))
	
b.sort()

for i in range(a):
	print(b[i])

	
"""
10
5
2
3
1
4
2
3
5
1
7
"""

