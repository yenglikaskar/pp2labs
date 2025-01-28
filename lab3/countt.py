#count
def k(grams):
    ounces = 28.3495231 * grams
    print (ounces)
grams = int(input())
k(grams)



#howmany
def solve(numheads = 35, numlegs = 94):
   
    # c + r = nh        c = nh - r
    # 4r + 2c = nl     4r = nl - 2nh + 2r             r = (nl - 2nh)/2 
    r = (numlegs - 2 * numheads)/2
    c = numheads - r
    print(f"rabbits = {r}, chicken = {c}")

solve()