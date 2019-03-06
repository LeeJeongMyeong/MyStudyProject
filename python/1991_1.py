n = int(input())
tree = []

for i in range(n):
	tmp = input().split()
	tree.append(tmp)
	
findNode = 'A'
firstAnswer = ""
secondAnswer = ""
thirdAnswer = ""

def frontCircuit():
	global findNode
	global firstAnswer
	count = 0
	for count in range(n):
		if findNode == tree[count][0]:
			firstAnswer += tree[count][0]
			break
	
	if tree[count][1] != '.':
		findNode = tree[count][1]
		frontCircuit()
		
	if tree[count][2] != '.':
		findNode = tree[count][2]
		frontCircuit()	

def middleCircuit():
	global findNode
	global secondAnswer
	
	count = 0
	for count in range(n):
		if findNode == tree[count][0]:
			break;
			
	if tree[count][1] != '.':
		findNode = tree[count][1]
		middleCircuit()
		
	secondAnswer += tree[count][0]
	
	if tree[count][2] != '.':
		findNode = tree[count][2]
		middleCircuit()
		
def endCircuit():
	global findNode
	global thirdAnswer
	
	count = 0
	for count in range(n):
		if findNode == tree[count][0]:
			break;
			
	if tree[count][1] != '.':
		findNode = tree[count][1]
		endCircuit()
		
	if tree[count][2] != '.':
		findNode = tree[count][2]
		endCircuit()
		
	thirdAnswer += tree[count][0]
		
		
frontCircuit()

findNode = 'A'

middleCircuit()

findNode = 'A'

endCircuit()


print(firstAnswer)
print(secondAnswer)
print(thirdAnswer)

"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

ABDCEFG
DBAECFG
DBEGFCA

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
"""
