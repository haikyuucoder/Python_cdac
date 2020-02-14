string=input("Enter the string: ")
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
for i in range(0,len(string)):
	if(string[i]=='a' ):
		count_a=count_a+1
	if(string[i]=='e' ):
		count_e=count_e+1
	if(string[i]=='i' ):
		count_i=count_i+1
	if(string[i]=='o' ):
		count_o=count_o+1
	if(string[i]=='u' ):
		count_u=count_u+1
print("Total vowels:",(count_a+count_e+count_i+count_o+count_u))
print("Total 'a':",count_a)
print("Total 'e':",count_e)
print("Total 'i':",count_i)
print("Total 'o':",count_o)
print("Total 'u':",count_u)