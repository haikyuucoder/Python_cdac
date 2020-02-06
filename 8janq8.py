num=int(input("Enter number n "))
sum=0
j=1
for i in range(1,num+1):
	sum=sum+j**2
	j=j+3
print(sum)