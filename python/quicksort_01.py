#import sys
#sys.setrecursionlimit(10000)

def quick(n):
	if len(n) <= 0:
		return 0
	p = len(n) - 1

	i = 0
	j = p - 1

	while True:
		if i >= j:
			break

		if n[i] > n[p] and n[j] <= n[p]:
			tmp = n[i]
			n[i] = n[j]
			n[j] = tmp
			i += 1
			j -= 1
		elif n[i] <= n[p] and n[j] > n[p]:
			i += 1
			j -= 1
		elif n[i] > n[p] and n[j] > n[p]:
			j -= 1
		elif n[i] < n[p] and n[j] < n[p]:
			i += 1
	

	tmp = n[i]
	n[i] = n[p]
	n[p] = tmp
	
	if i > 0:
		left = n[0:i-1]
		quick(left)
	
	right = n[i:]
	quick(right)
	


k = input().split()

quick(k)

print(k)


"""

5 3 7 6 2 1 4

"""