var=str(input("Enter a string: "))
strlen=len(var)
new_str=""
for i in range(strlen-1,-1,-1):
	new_str=new_str+var[i]
if(new_str==var):
	print("It is a palindrome")
else:
	print("It is not palindrome")