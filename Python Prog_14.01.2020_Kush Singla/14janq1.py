#Enter 15 numbers by user in a list and then find if a number (also entered by user) is in the list or not

print("Enter 15 numbers: ")
l=[]
for i in range(15):
	l.append(float(input()))
num=float(input("Enter the number you want to find: "))
m=0
for i in range(len(l)):
	if(l[i]==num):
		if(m!=0):
			print(",",end="")
		if(m==0):
			print(num,"is at index:",end=" ")
		print(i,end='')
		m=m+1
if(m==0):
	print(num,"is not present in the list")
		


