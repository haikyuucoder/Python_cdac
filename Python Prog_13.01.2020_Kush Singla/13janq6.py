string=input("Enter the string: ")
list=[0]*128
for i in string:
	list[ord(i)]=list[ord(i)]+1	
for j in range(128):
	if(list[j]!=0):
		print(chr(j),":",list[j])
	else:
		continue