
list_sin=[]
list_cos=[]
list_tan=[]
import math
for i in range(30,91,30):
	list_sin.append(math.sin(math.radians(i)))
	list_cos.append(math.cos(math.radians(i)))
	list_tan.append(math.tan(math.radians(i)))

print("%4s"%'',"%11s"%'30 degrees',"%11s"%'60 degrees',"%11s"%'90 degrees')
print("Sin",end=" ")
for i in range(3):
	print("%11.2f"%list_sin[i],end="")
print()
print("Cos",end=" ")
for i in range(3):
	print("%11.2f"%list_cos[i],end="")
print("\n","Tan",sep="",end=" ")
for i in range(3):
	if(i!=2):
		print("%11.2f"%list_tan[i],end="")
	else:
		print("%25s"%list_tan[i],end=" ")
