import sys

a = int(input())

if a < 1:
	sys.exit(1)
if a > 1000:
	sys.exit(1)

b = input().split()

b.sort()

result = 0
hap = 0
for i in range(a):
	hap += int(b[i])
	result = result + hap
	
print(result)






"""

3 
3 + 1
3 + 1 + 4



5
3 1 4 3 2
"""