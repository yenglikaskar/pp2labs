def double_numbers(nums):
    nums = list(map(lambda x: 2*x,nums))
    return nums
nums = list(map(int, input().split()))
print(double_numbers(nums))

new_list = [x * 2 for x in nums ]
print(new_list)