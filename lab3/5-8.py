#revstring
def reverse(a):
    each = a.split()
    print (*each[:: -1])
a = input()
reverse(a)

#3next
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[1 + i] == 3:
            return True
    return False
nums = list(map(int, input().split()))
print(has_33(nums))


#007
def spy_game(lisst):
    for i in range(len(lisst) - 2):
        if lisst[i] == 0 and lisst[1 + i] == 0 and lisst[i + 2] == 7:
            return True
    return False
nums = list(map(int, input().split()))
print(has_33(nums))
    