string=input("Enter the string: ")
if(len(string)%2==0):
	for i in range(0,int(len(string)/2)):
		print(string[i],end="")
else:
	print("null")