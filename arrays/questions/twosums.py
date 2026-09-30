# ============================================================
# TWO SUM
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#   Reason: nums[0] + nums[1] = 2 + 7 = 9
#
# Example 2:
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]
#
# Example 3:
#   Input:  nums = [3, 3], target = 6
#   Output: [0, 1]
#
# Constraints:
#   - 2 <= nums.length <= 10^4
#   - -10^9 <= nums[i] <= 10^9
#   - -10^9 <= target <= 10^9
#   - Only one valid answer exists

# ------------------------------------------------------------
# APPROACH — Brute Force (Nested Loop)
# ------------------------------------------------------------
# - Keep a fixed and move b through every element after a
# - For every pair (a, b), check if nums[a] + nums[b] == target
# - If yes, return [a, b]
#
# Time Complexity  : O(n²) — two nested loops, every pair is checked
# Space Complexity : O(1)  — no extra space used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

def twoSum(nums, target):
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

print(twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(twoSum([3, 2, 4], 6))        # Expected: [1, 2]
print(twoSum([3, 3], 6))           # Expected: [0, 1]

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Loop over indices using range(len(nums)), not values directly
# - b starts at a+1 to avoid pairing an element with itself
#   and to avoid checking the same pair twice
# - This is O(n²) — there is a faster O(n) solution using HashMap
#   which will be revisited when HashMaps are covered