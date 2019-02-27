import queue
q = queue.Queue()

a = int(input())

for i in range(a):
	q.put(i+1)
	
while q.qsize() > 1 :
	q.get()
	b = q.get()
	q.put(b)
	
print(q.get())