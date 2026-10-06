# ============================================================
# MAXIMUM SUBARRAY
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array nums, find the subarray with the
# largest sum and return its sum.
#
# A subarray is a contiguous sequence of elements — no gaps,
# elements must be next to each other.
#
# Example 1:
#   Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: 6
#   Reason: Subarray [4, -1, 2, 1] has the largest sum 6
#
# Example 2:
#   Input:  nums = [1]
#   Output: 1
#
# Example 3:
#   Input:  nums = [5, 4, -1, 7, 8]
#   Output: 23
#
# Constraints:
#   - 1 <= nums.length <= 10^5
#   - -10^4 <= nums[i] <= 10^4

# ------------------------------------------------------------
# APPROACH — Kadane's Algorithm
# ------------------------------------------------------------
# At every element, ask one question:
#   "Is my current running sum helping or hurting me?"
#
# If current_sum goes negative → reset to 0 (start fresh)
# If current_sum is positive   → keep adding to it
# At every step → update max_sum if current_sum is better
#
# Key: update max_sum BEFORE resetting current_sum
#      otherwise you miss negative numbers that are still the best answer
#
# max_sum starts at -infinity to handle all-negative arrays
# (if it started at 0, an all-negative array would wrongly return 0)
#
# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — only two variables used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
print(s.maxSubArray([1]))                                 # Expected: 1
print(s.maxSubArray([5, 4, -1, 7, 8]))                   # Expected: 23
print(s.maxSubArray([-1, -2, -3]))                        # Expected: -1

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - A subarray must be contiguous — can't skip elements
# - Kadane's: if running sum goes negative, reset to 0 and start fresh
# - A negative running sum is dead weight — always better to start fresh
# - Update max_sum BEFORE resetting current_sum — order matters
# - max_sum starts at -infinity not 0 — handles all-negative arrays
# - One loop, two variables — O(n) time, O(1) space