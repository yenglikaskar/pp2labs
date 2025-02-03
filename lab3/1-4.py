#count
def k(grams):
    ounces = 28.3495231 * grams
    print (ounces)
grams = int(input())
k(grams)


#fahrenheit
def fahr(f):
    c = (5 / 9) * (f - 32)
    print(c)

f = int(input())
fahr(f)


#howmany
def solve(numheads = 35, numlegs = 94):
   
    # c + r = nh        c = nh - r
    # 4r + 2c = nl     4r = nl - 2nh + 2r             r = (nl - 2nh)/2 
    r = (numlegs - 2 * numheads)/2
    c = numheads - r
    print(f"rabbits = {r}, chicken = {c}")

solve()

#prime
def is_prime(num):
    prime = []
    for i in num:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1 
        if count == 0:
            prime.append(i) 
    print(prime)
num = list(map(int, input().split()))
is_prime(num)