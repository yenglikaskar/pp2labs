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
def prime(num):
    prime = True

    if num < 2:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
def is_prime(general):
    pass
