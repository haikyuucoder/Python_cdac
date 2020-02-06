a=int(input("Enter 1st number " ))
b=int(input("Enter 2nd number " ))
c=int(input("Enter 3rd number " ))
if a>b:
	if a>c:
		print(a,"is the greatest number")
	else :
		print(c,"is the greatest number")
else:
	if c>b:
		print(c,"is the greatest number")
	else:
		print(b,"is the greatest number")