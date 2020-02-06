num=int(input("Enter the number n "))
sum=0
total=0
if num>7:
	for i in range(1,num+1):
		if i%7==0:
			sum=sum+i
			total=total+1

	print("The sum of numbers divisible by 7 in the first n numbers is:",sum)
	print("The average of the numbers divisible by 7 in the first n numbers is:",sum/total)
elif num>0 and num<7:
	print("The sum of numbers divisible by 7 in the first n numbers is:0")
	print("The average of the numbers divisible by 7 in the first n numbers is 0")
else:
	print("Enter valid number")