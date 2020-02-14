a=input("Enter 1st string: ")
b=input("Enter 2nd string: ")
if(len(a)>len(b)):
	t=len(a)
else:
	t=len(b)
for i in range(0,t):
	if(i<len(a) and i<len(b)):
		print(a[i],b[i],sep="",end="")
	else:
		if(len(a)>len(b)):
			print(a[i],end="")
		else:
			print(b[i],end="")
