#volume
def v(r):
    vol = (4 * 3.14 * r**3)/3
    print("Volume:", vol)
#r = int(input())
#v(r)

#unique
def sortt(mylist):
    pass

#palindrome

#histogram
def histogram(l):
    for i in l:
        for j in range(i):
            print('*', end = '')
        print()
l = list(map(int, input().split()))
histogram(l)