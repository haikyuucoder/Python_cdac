gadgets=["Mobile","Laptop",100,"Camera",310.28,"Speakers",27.00,"Television",1000,"Laptop Case","Camera Lens"]
strList=[]
numList=[]
for i in range(len(gadgets)):
	if(type(gadgets[i])==str):
		strList.append(gadgets[i])
	if(type(gadgets[i])==float or type(gadgets[i])==int):
		numList=numList + [gadgets[i]]
print("List of Strings and Numbers:")
print(strList)
print(numList)
print()


a=sorted(strList)
print("Sorted list of Strings(Ascending):\n",a,"\n")
a=sorted(strList,reverse=True)
print("Sorted list of Strings(Descending):\n",a,"\n")
a=sorted(numList)
print("Sorted list of Numbers(Highest to Lowest):\n",a,"\n")
a=sorted(numList,reverse=True)
print("Sorted list of Numbers(Lowest to Highest):\n",a,'\n')
