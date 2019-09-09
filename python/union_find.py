def union(x, y):
	a = find(x)
	b = find(y)

	if a[1] != b[1]:
		b[1] = a[1]
		

def find(z):
	if t[z][0] != t[z][1]:
		return find(t[z][1])
	else :
		return t[z]



a = input().split()
g = []
t = []
val = []
#for i in range(int(a[1])):
#	g.append(input().split())

for i in range(int(a[0])):
	t.append([i,i])

print(t)
union(1, 2)
print(t)
union(0, 1)
print(t)

"""
3 3
1 2 1
2 3 2
1 3 3
"""
