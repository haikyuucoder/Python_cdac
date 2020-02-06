num=int(input("Enter the number n of which you want to find the factorial"))
fact=1
numTemp=num
if num<0:
	print("Invalid number")
elif num>0:
	while num!=1:
		fact=fact*num
		num=num-1
print("!",end="")
print(numTemp,"=",fact)