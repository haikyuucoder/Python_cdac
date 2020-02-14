import math
radius=float(input("Enter radius of the circle: "))
if(radius>=0):
	area=(math.pi)*(radius**2)
	print("Area of the circle is:",area)
else:
	print("Enter valid number for radius")