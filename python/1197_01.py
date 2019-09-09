#import sys; sys.setrecursionlimit(100)


def union(x, y):
	a = find(x-1)
	b = find(y-1)

	if a[1] != b[1]:
		b[1] = a[1]
		return True
	return False;
		

def find(z):
	if int(t[z][0]) != int(t[z][1]):
		return find(t[z][1]-1)
	else :
		return t[z]

a = input().split()
g = []
t = []
hap = 0
for i in range(int(a[1])):
	g.append(input().split())

g.sort(key = lambda x:x[2])

for i in range(int(a[0])):
	t.append([i+1,i+1])

for i in range(int(a[1])):
	if union(int(g[i][0]), int(g[i][1])):
		hap += int(g[i][2])

print(hap)
"""
3 3
1 2 1
2 3 2
1 3 3
"""
