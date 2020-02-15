#Input two matrices from the user, perform addition if possible and then print the final matrix

print("Enter the 1st matrix(enter 'c' when you have completely entered the matrix): ")
matrix1=[]
j=['a']
m1=0
while j[0]!='c':
	row=input().split()
	j[0]=row[0]
	if(j[0]=='c'):
		continue
	if(m1!=0):
		if(a1!=len(row)):
			print("Maintain the same number of elements in each row",end="")
			exit()
	m1=m1+1
	a1=len(row)
	print(row)
	for i in range(len(row)):
		row[i]=int(row[i])
	matrix1.append(row)
print("First Matrix:",m1,"X",a1,"matrix")
for j in range(len(matrix1)):
	print(matrix1[j])
print("Enter the 2nd matrix(enter 'c' when you have completely entered the matrix): ")
matrix2=[]
j=['a']
m2=0
while j[0]!='c':
	row=input().split()
	j[0]=row[0]
	if(j[0]=='c'):
		continue
	if(m2!=0):
		if(a2!=len(row)):
			print("Maintain the same number of elements in each row",end="")
			exit()
	m2=m2+1
	a2=len(row)
	print(row)
	for i in range(len(row)):
		row[i]=int(row[i])
	matrix2.append(row)
print("Second Matrix:",m2,"X",a2,"matrix")
for j in range(len(matrix2)):
	print(matrix2[j])
matrix=[]
list=[]
if(m1==m2 and a1==a2):
	print("Matrix after adding:")
	for i in range(m1):
		for l in range(a1):
			list.append(matrix1[i][l]+matrix2[i][l])
		matrix.append(list)
		print(list)
		list=[]
else:
	print("Since rows and columns are not same of both the matrices,addition cannot be performed")

