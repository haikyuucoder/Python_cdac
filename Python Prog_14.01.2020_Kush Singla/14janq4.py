#Input a matrix from user and print the transpose of that matrix.

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
print("Transpose of the matrix:")
temp=0
q=0
for i in range(0,m):
	for j in range(q,a):
		temp=matrix[i][j]
		matrix[i][j]=matrix[j][i]
		matrix[j][i]=temp
	q=q+1
for j in range(len(matrix)):
	print(matrix[j])