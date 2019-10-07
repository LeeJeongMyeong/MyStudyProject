import queue

q = queue.Queue()
a = input().split()

n = int(a[0])
k = int(a[1])

count = 0

q.put([n,count])

while q:
	tmp = q.get()
	x = tmp[0]
	y = tmp[1]
	
	if x == k:
		count = y
		break
	
	y += 1
	q.put([x*2, y])
	q.put([x+1, y])
	q.put([x-1, y])
	
	


print(count)