#1
def gen_sq(n):
    for i in range(n + 1):
        yield i*i
n = int(input())
print("squares:")
for i in gen_sq(n):
    print(i)


#2
def even(k):
    for i in range(1,k + 1):
        if i % 2 == 0:
            yield i
k = int(input())
print("even:")
for i in even(k):
    print(i)


#3
def div(a):
    for i in range(0, a + 1):
        if i % 4 == 0 and i % 3 == 0:
            yield i
a = int(input())
print("nums divisible by 3 and 4:")
for i in div(a):
    print(i)


#4
def area_square(a,b):
    for i in range(a, b + 1):
        yield i **2

a = int(input("between "))
b = int(input("and "))
for i in area_square(a, b):
    print(i)


#5
def down(l):
    while l >= 0:
        yield l
        l -= 1
l = int(input())
print(f"from:{l} to 0 ")
for i in down(l):
    print(i)
