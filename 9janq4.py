sum=0
import random
for i in range(1,11):
	x=random.random()*100
	if(x<1):
		i=i-1
	sum=sum+x
	print(x)
print(sum)
