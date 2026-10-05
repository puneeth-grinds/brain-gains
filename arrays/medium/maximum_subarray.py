nums = [5,4,-1,7,8]
current_sum = 0
max_sum = float('-inf')

for i in range(len(nums)):
    current_sum = current_sum + nums[i]
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(max_sum)
    