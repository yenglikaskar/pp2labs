#volume
def v(r):
    vol = (4 * 3.14 * r**3)/3
    print("Volume:", vol)
r = int(input())
v(r)

#unique
def unique_elements(first_list):
    new_list = [first_list[0]]
    for item in first_list:
        if item not in new_list:
            new_list.append(item)
    print("New list", new_list)

enter = list(map(int, input().split()))
unique_elements(enter)

#palindrome
def palindrome(word):
    rev = word[::-1]
    return rev == word
word = input()
print(palindrome(word))


#histogram
def histogram(l):
    for i in l:
        for j in range(i):
            print('*', end = '')
        print()
l = list(map(int, input().split()))
histogram(l)