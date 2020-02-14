word=input("Enter word,seperator and count: ")
seperator=input()
count=int(input())
if(count>=0):
	for i in range(1,count+1):
		print(word,seperator,sep="",end="")
else:
	print("Count value Invalid!")