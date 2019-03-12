"""it is anser...
	bur not my code... :("""

n = int(input())

result = [[0 for i in range(3)] for i in range(n)]

firstInput = input().split()

result[0][0] = int(firstInput[0])
result[0][1] = int(firstInput[1])
result[0][2] = int(firstInput[2])

for i in range(n - 1):
	temp = input().split()
	result[i+1][0] = int(temp[0]) + min(result[i][1], result[i][2])
	result[i+1][1] = int(temp[1]) + min(result[i][0], result[i][2])
	result[i+1][2] = int(temp[2]) + min(result[i][0], result[i][1])
	
print(min(result[n-1][0], result[n-1][1], result[n-1][2]))

"""
3
26 40 83
49 60 57
13 89 99
96

"""