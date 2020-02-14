import math
point1x=float(input("Enter x of point 1: "))
point1y=float(input("Enter y of point 1: "))
point2x=float(input("Enter x of point 2: "))
point2y=float(input("Enter y of point 2: "))
x=point1x-point2x
y=point1y-point2y
print("The distance between the two points is:",math.hypot(x,y))