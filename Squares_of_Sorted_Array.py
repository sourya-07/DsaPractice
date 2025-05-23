# Using two pointer approach :-


nums = list(map(int, input().split()))
left = 0
right = len(nums) - 1
result = [0] * len(nums)

for i in range(len(nums) - 1, -1, -1):
    if nums[left] ** 2 > nums[right] ** 2:  
        result[i] = nums[left] ** 2
        left += 1
    else:
        result[i] = nums[right] ** 2
        right -= 1
    print(result)