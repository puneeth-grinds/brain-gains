# ============================================================
# 3SUM
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array nums, return all unique triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k
# and nums[i] + nums[j] + nums[k] == 0.
# The solution must not contain duplicate triplets.
#
# Example 1:
#   Input:  nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#
# Example 2:
#   Input:  nums = [0, 1, 1]
#   Output: []
#
# Example 3:
#   Input:  nums = [0, 0, 0]
#   Output: [[0, 0, 0]]
#
# Constraints:
#   - 3 <= nums.length <= 3000
#   - -10^5 <= nums[i] <= 10^5

# ------------------------------------------------------------
# APPROACH — Sort + Two Pointers
# ------------------------------------------------------------
# Fix one number at a time (i) and use two pointers (left, right)
# to find the other two that sum to -nums[i].
#
# Step 1 — Sort the array
#           Sorting enables two pointer logic and makes duplicate
#           skipping easy since duplicates sit next to each other
#
# Step 2 — Fix i, search with left and right
#           left starts at i+1, right starts at end
#           sum < 0 → move left forward (need bigger number)
#           sum > 0 → move right backward (need smaller number)
#           sum == 0 → found triplet, move both inward
#
# Step 3 — Skip duplicates at three levels
#           i     → skip if nums[i] == nums[i-1]
#           left  → skip if nums[left] == nums[left-1] after finding triplet
#           right → skip if nums[right] == nums[right+1] after finding triplet
#
# Time Complexity  : O(n²) — outer loop O(n), inner two pointer O(n)
# Space Complexity : O(1)  — ignoring output list

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))   # Expected: [[-1,-1,2],[-1,0,1]]
print(s.threeSum([0, 1, 1]))                # Expected: []
print(s.threeSum([0, 0, 0]))               # Expected: [[0,0,0]]
print(s.threeSum([1, 2, 0, 1, 0, 0, 0]))   # Expected: [[0,0,0]]

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Sort first — enables two pointer logic and easy duplicate skipping
# - Fix one number (i), find other two with left and right pointers
# - sum < 0 → left moves right (need bigger), sum > 0 → right moves left
# - Three levels of duplicate skipping needed — i, left, and right
# - i=0 edge case: use i > 0 before comparing nums[i] with nums[i-1]
# - result.append([...]) — needs a list inside, not three separate args
# - return must be outside the for loop, not inside