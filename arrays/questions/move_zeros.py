# ============================================================
# MOVE ZEROES
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note: Must be done in-place without making a copy of the array.
#
# Example 1:
#   Input:  nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
#
# Example 2:
#   Input:  nums = [0]
#   Output: [0]
#
# Constraints:
#   - 1 <= nums.length <= 10^4
#   - -2^31 <= nums[i] <= 2^31 - 1

# ------------------------------------------------------------
# APPROACH — Two Step
# ------------------------------------------------------------
# Instead of moving zeros to the end, flip the thinking:
# move all non-zero elements to the front, then fill the rest with zeros.
#
# Step 1 — use a position pointer (pos) starting at 0
#           every time a non-zero is found, place it at pos and move pos forward
# Step 2 — fill everything from pos to end with 0
#
# Time Complexity  : O(n) — two passes through the array
# Space Complexity : O(1) — in-place, no extra space used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[pos] = nums[i]
            pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

        return nums


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))   # Expected: [1, 3, 12, 0, 0]
print(s.moveZeroes([0]))                 # Expected: [0]
print(s.moveZeroes([1, 0, 0, 3, 0]))    # Expected: [1, 3, 0, 0, 0]

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Don't modify an array while iterating — elements shift and you skip values
# - Flip the problem: instead of moving zeros back, move non-zeros to the front
# - pos pointer tracks where the next non-zero should be placed
# - for loops auto-increment — no need to manually do i = i + 1
# - In-place means O(1) space — work within the same array, no copies