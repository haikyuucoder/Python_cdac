num=int(input("Enter the number of elements in the list of integers: "))
l=[]
for i in range(1,num+1):
	print("Enter element number",i)
	l=l+[int(input())]
print("The list is:",l)

num=int(input("Enter the number of elements in the list of strings: "))
l=[]
for i in range(1,num+1):
	print("Enter element number",i)
	l=l+[input()]
print("The list is:",l)
	