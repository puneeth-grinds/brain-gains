# ============================================================
# REMOVE ELEMENT
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-element/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The order of the elements
# may be changed. Return k — the number of elements not equal to val.
#
# The first k elements of nums should contain elements not equal to val.
# Everything beyond index k-1 can be ignored.
#
# Example 1:
#   Input:  nums = [3, 2, 2, 3], val = 3
#   Output: k = 2, nums = [2, 2, _, _]
#
# Example 2:
#   Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
#   Output: k = 5, nums = [0, 1, 3, 0, 4, _, _, _]
#
# Constraints:
#   - 0 <= nums.length <= 100
#   - 0 <= nums[i] <= 50
#   - 0 <= val <= 100

# ------------------------------------------------------------
# APPROACH — Position Pointer
# ------------------------------------------------------------
# k acts as a position pointer tracking where to place
# the next element that is not equal to val.
#
# For every element i walks through —
#   if nums[i] == val → skip it
#   if nums[i] != val → place it at k, move k forward
#
# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — in-place, no extra space used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k] = nums[i]
            k += 1
        return k


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))           # Expected: 2
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Expected: 5
print(s.removeElement([1], 1))                     # Expected: 0
print(s.removeElement([1], 2))                     # Expected: 1

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Same position pointer pattern as Move Zeroes and Remove Duplicates
# - Only difference is the condition — skip if nums[i] == val
# - nums[k] = nums[i] overwrites, it does not remove — array size stays the same
# - Everything beyond index k-1 is ignored by LeetCode
# - The pointer pattern: i walks through everything, k only moves on a valid element