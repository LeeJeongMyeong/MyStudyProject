def quick(n):
	if len(n) > 1:
		p = n[len(n)-1]
		left, mid, right = [], [], []
		
		for i in range(len(n)-1):
			if n[i]< p:
				left.append(n[i])
			elif n[i] > p:
				right.append(n[i])
			else:
				mid.append(n[i])
				
		mid.append(p)
		return quick(left) + mid + quick(right)
	else:
		return n

	
k = input().split()

print(quick(k))


"""

5 3 7 6 2 1 4

"""