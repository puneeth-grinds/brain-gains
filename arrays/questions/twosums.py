nums = nums = [2, 4, 3, 7]
target = 9

for a in range(len(nums)):
    for b in range(len(nums)):
        if nums[a] + nums[b] == target:
            print(a,b)                                                               