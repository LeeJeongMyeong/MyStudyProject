n = []
for i in range(9):
	n.append(int(input()))
	
a = b = c = d = e = f = g = 0
check = False
for a in range(9):
	for b in range(a+1, 9):
		for c in range(b+1, 9):
			for d in range(c+1, 9):
				for e in range(d+1, 9):
					for f in range(e+1, 9):
						for g in range(f+1, 9):
							if n[a]+n[b]+n[c]+n[d]+n[e]+n[f]+n[g] == 100:
								check = True
								break
						if check:
							break
					if check:
						break
				if check:
					break
			if check:
				break
		if check:
			break
	if check:
		break
		
answer = [n[a], n[b], n[c], n[d], n[e], n[f], n[g]]
answer.sort()

print(answer)

"""
20
7
23
19
10
15
25
8
13
"""