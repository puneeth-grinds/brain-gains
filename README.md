# brain-gains
Structured DSA prep
for i in range(len(nums)):
    current_sum = current_sum + nums[i] //-
    if current_sum < 0:
        current_sum = 0
    else:
        if current_sum > max_sum:
            max_sum = current_sum
print(max_sum)