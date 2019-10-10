n = int(input())

t = input().split()
t.sort()

answer = 0
tmp = 0
for i in range(n):
	tmp	+= int(t[i])
	answer += tmp
	
print(answer)

"""
5
3 1 4 3 2
"""