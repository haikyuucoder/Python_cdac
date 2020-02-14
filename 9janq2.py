import math
for i in range(0,91,15):
	if(i==15 or i==75):
		continue
	print("sin(",i,"degree)",sep="",end=" ")
	print(math.sin(math.radians(i)))
	print("cos(",i,"degree)",sep="",end=" ")
	print(math.cos(math.radians(i)))
	print("tan(",i,"degree)",sep="",end=" ")
	print(math.tan(math.radians(i)))
	print()
	