# ============================================================
# REMOVE DUPLICATES FROM SORTED ARRAY
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once. The relative order should be kept the same.
#
# Return k — the number of unique elements.
# The first k elements of nums should contain the unique numbers.
# Everything beyond index k-1 can be ignored.
#
# Example 1:
#   Input:  nums = [1, 1, 2]
#   Output: k = 2, nums = [1, 2, _]
#
# Example 2:
#   Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#   Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# Constraints:
#   - 1 <= nums.length <= 3 * 10^4
#   - -100 <= nums[i] <= 100
#   - nums is sorted in non-decreasing order

# ------------------------------------------------------------
# APPROACH — Two Pointers
# ------------------------------------------------------------
# Since the array is sorted, duplicates always sit next to each other.
# So comparing nums[i] with nums[i-1] is enough to detect duplicates.
#
# i   → walks through every element one by one
# pos → tracks where to place the next unique element
#
# They start together at 1 (first element is always unique).
# pos only moves forward when a unique element is found.
# i moves forward every step regardless.
# The gap between i and pos is where duplicates pile up.
#
# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — in-place, no extra space used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def removeDuplicates(self, nums):
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pos] = nums[i]
                pos += 1
        return pos


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.removeDuplicates([1, 1, 2]))                    # Expected: 2
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Expected: 5
print(s.removeDuplicates([1]))                          # Expected: 1

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Sorted array = duplicates are always neighbours, so compare i with i-1
# - Two pointers serve two separate jobs — i walks, pos places
# - pos only moves when a unique element is found, i always moves
# - The gap between i and pos is where duplicates accumulate — that's fine
# - Don't use pop() inside a loop — it shifts elements and causes skips
# - In-place means O(1) space — no new array, work on the original