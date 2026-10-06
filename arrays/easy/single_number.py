# ============================================================
# SINGLE NUMBER
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.
#
# Must be solved in O(n) time and O(1) space.
#
# Example 1:
#   Input:  nums = [2, 2, 1]
#   Output: 1
#
# Example 2:
#   Input:  nums = [4, 1, 2, 1, 2]
#   Output: 4
#
# Example 3:
#   Input:  nums = [1]
#   Output: 1
#
# Constraints:
#   - 1 <= nums.length <= 3 * 10^4
#   - -3 * 10^4 <= nums[i] <= 3 * 10^4
#   - Every element appears twice except for one

# ------------------------------------------------------------
# APPROACH — XOR
# ------------------------------------------------------------
# XOR has two magic properties:
#   - Same number XOR itself = 0  (e.g. 4 ^ 4 = 0)
#   - Any number XOR 0 = itself   (e.g. 4 ^ 0 = 4)
#
# XOR every element together — every duplicate pair cancels
# itself out to 0. The single number has no pair to cancel
# with, so it survives and is returned.
#
# Example:
#   [4, 1, 2, 1, 2]
#   = 4 ^ (1^1) ^ (2^2)
#   = 4 ^ 0 ^ 0
#   = 4 ✅
#
# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — only one variable used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.singleNumber([2, 2, 1]))          # Expected: 1
print(s.singleNumber([4, 1, 2, 1, 2]))    # Expected: 4
print(s.singleNumber([1]))                # Expected: 1

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - XOR operates at the bit level — same bits cancel to 0, different give 1
# - Same number XOR itself always = 0
# - Any number XOR 0 = itself
# - Every duplicate pair destroys itself — only the single number survives
# - No extra space needed — one variable, one pass, done