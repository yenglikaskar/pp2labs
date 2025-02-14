import math
#1
d = int(input("degree: "))
r = d * math.pi / 180
print("radian: ", r)


#2
h = int(input("height: "))
f = int(input("first value:"))
s = int(input("second value:"))
a = (f + s)*0.5*h
print("area", a)

#3
s = int(input("sides: "))
l = int(input("length: "))
area = (s * (l**2) * (1/math.tan(math.pi / s))) / 4 
print("area", int(area))

#4
l = int(input("Length of base:"))
h = int(input("Height of parallelogram:"))
ap = l*h
print ("area of the parallelogram: ", float(ap))
