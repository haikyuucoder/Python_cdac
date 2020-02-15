num=int(input("Enter number of elements in list:"))
l=[]
for i in range(num):
	l=l+[float(input())]
print("Largest:",max(l))
print("Smallest:",min(l))