from collections import deque
q = deque()

a = input().split()
hyung = int(a[0])
dongsang = int(a[1])
#print(a)

q.append([hyung, 0])

#print(len(checker))
checker = [False for i in range(1000000)]

#print(q)
tmp = []
while q:
	tmp = q.popleft()
	
	where = int(tmp[0])
	count = int(tmp[1])
	
	if(checker[where] == True):
		continue
	
	checker[where] = True
	
	if(where == dongsang):
		break
		
	if(where > 0):
		q.append([where-1, count+1])
	if(where < dongsang):
		q.append([where+1, count+1])
		q.append([where*2, count+1])
		
print(tmp[1])