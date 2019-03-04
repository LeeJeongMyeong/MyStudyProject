def answer(inputWord):
	global word
#asdfasdfasdf fdsafdsafdsa asdffdsaasdffdsaasdffdsa
	flag = False
	while word:
		wordTemp = word.pop(0)
		count = len(wordTemp[0])
		lastWordCount = wordTemp[1][len(wordTemp[1])-1]
		for k in range(len(inputWord[2])):
			if((inputWord[0][count] == inputWord[2][k]) and lastWordCount < k):
				word.append([wordTemp[0]+inputWord[0][count], wordTemp[1] + [k]])
		
		for k in range(len(word)):
			if (len(word[k][1]) == len(inputWord[0])):
				tmp = list(inputWord[2][:])
				tmpCount = word[k][1][:]
				tmpCount.reverse()
				
				for x in range(len(tmpCount)):
					tmp.pop(tmpCount[x])
				
				if tmp == list(inputWord[1]):
					flag = True;
					
			if flag:
				break
		
		if flag:
			break
	return flag
		
n = int(input())

word = []

for i in range(n):
	inputWord = input().split()
	
	for j in range(len(inputWord[2])):
		if(inputWord[0][0] == inputWord[2][j]):
			word.append([inputWord[0][0],[j]])
	
	if answer(inputWord):
		print ("Data set ",i+1,": yes")
		word = []
	else : 
		print ("Data set ",i+1,": no")
		word = []
		
"""
3
cat tree tcraete
cat tree catrtee
cat tree cttaree
"""