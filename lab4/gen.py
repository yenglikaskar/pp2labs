def gen_sq(n):
    for i in range(n + 1):
        yield i*i
n = int(input())
for i in gen_sq(n):
    print(i)
