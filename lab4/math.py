import math
d = int(input("degree: "))
r = d * math.pi / 180
print("radian: ", r)

h = int(input("height: "))
f = int(input("first value:"))
s = int(input("second value:"))
a = (f + s)*0.5*h
print("area", a)

s = int(input("sides: "))
l = int(input("length: "))
area = (s * (l**2) * (1/math.tan(math.pi / s))) / 4 
print("area", int(area))