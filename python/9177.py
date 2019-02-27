n = int(input())

for i in range(n):
	temp = input().split()
	
	count = 0
	flag = False
	firstWord = ""
	secondWord = ""
	for j in range(len(temp[2])):
		if (temp[0][count] == temp[2][j]):
			firstWord += temp[2][j]
			count += 1
		else:
			secondWord += temp[2][j]
		
		if(len(temp[0]) == len(firstWord)):
			secondWord += temp[2][j+1:]
			if (temp[0] == firstWord and temp[1] == secondWord):
				break
			else:
				count -= 1
				firstWord = firstWord[:count]
				secondWord = secondWord[:j]
				print("middle : ", firstWord, " : " , secondWord)
			
			
	print(firstWord, " : " , secondWord)
	if (temp[0] == firstWord and temp[1] == secondWord):
		print ("Data set ",i+1,": yes")
	else : 
		print ("Data set ",i+1,": no")



"""
3
cat tree tcraete
cat tree catrtee
cat tree cttaree



Data set 1: yes
Data set 2: yes
Data set 3: no
"""