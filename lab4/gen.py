def gen_sq(n):
    for i in range(n + 1):
        yield i*i
n = int(input())
print("squares:")
for i in gen_sq(n):
    print( i)


def even(k):
    for i in range(1,k + 1):
        if (i % 2 == 0):
            yield i
k = int(input())
print("even:")
for i in even(k):
    print(i)

