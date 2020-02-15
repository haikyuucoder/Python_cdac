num=int(input("Enter the number of elements in list: "))
l=[]
for i in range(num):
	l=l+[float(input())]
a=sorted(l)
if(num%2==0):
	print("Median:",(a[int(num/2)]+a[int(num/2)+1])/2)
else:
	print("Median:",a[round(num/2)+1])
