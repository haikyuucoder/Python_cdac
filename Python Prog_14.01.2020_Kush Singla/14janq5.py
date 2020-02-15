#Matrix Multiplication(Input two matrices from a user, perform matrix multiplication if possible,then print the final matrix)

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
row=[]
matrix_final=[]
if(a1==m2):
	print("The Matrix after Multiplication is:")
	for h1 in range(m1):
		for h2 in range(a2):
			sum=0
			for k in range(0,m2):
				sum=sum+matrix1[h1][k]*matrix2[k][h2]
			row.append(sum)
		matrix_final.append(row)
		row=[]
	for j in range(len(matrix_final)):
		print(matrix_final[j])
else:
	print("The matrices cannot be multiplied as one is",m1,"X",a1,"and the other is",m2,"X",a2)