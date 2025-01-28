#fahrenheit
def fahr(f):
    c = (5 / 9) * (f - 32)
    print(c)

f = int(input())
fahr(f)




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
