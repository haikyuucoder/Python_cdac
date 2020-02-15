#Input a matrix from user and find the sum of diagonal elements.

print("Enter the matrix(enter 'c' when you have completely entered the matrix): ")
matrix=[]
j=['a']
m=0
while j[0]!='c':
	row=input().split()
	j[0]=row[0]
	if(j[0]=='c'):
		continue
	if(m!=0):
		if(a!=len(row)):
			print("Maintain the same number of elements in each row",end="")
			exit()
	m=m+1
	a=len(row)
	print(row)
	for i in range(len(row)):
		row[i]=int(row[i])
	matrix.append(row)
print(m,"X",a,"matrix")
for j in range(len(matrix)):
	print(matrix[j])
if(a>m):
	h=m
else:
	h=a
sum=0
for k in range(h):
	sum=sum+matrix[k][k]
if(a==m):
	print("The sum of diagonal elements is:",sum)
else:
	print("Since it is not a square matrix,sum of diagonal element does not exist")