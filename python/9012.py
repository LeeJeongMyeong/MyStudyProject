a = int(input())

answer = []

for i in range(a):
	b = list(input())
	c = 0
	enable = True
	for j in range(len(b)):
		d = b.pop()
		if j == 0 and d == "(":
			answer.append("NO")
			enable = False
			break
		elif d == "(" and c == 0:
			answer.append("NO")
			enable = False
			break
		elif d == "(":
			c = c - 1
		else:
			c = c + 1
		
	if c == 0 and enable == True:
		answer.append("YES")
	elif c != 0 and enable == True:
		answer.append("NO")

for i in range(len(answer)):
	print(answer[i])