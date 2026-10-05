# ============================================================
# CONTAINER WITH MOST WATER
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given an integer array height of length n, find two lines
# that together with the x-axis form a container that holds
# the most water. Return the maximum amount of water.
#
# Water fills up to the shorter wall — the taller one doesn't
# matter because water spills over the shorter one.
#
# Example 1:
#   Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
#   Reason: Lines at index 1 (height 8) and index 8 (height 7)
#           width=7, height=min(8,7)=7, area=49
#
# Example 2:
#   Input:  height = [1, 1]
#   Output: 1
#
# Constraints:
#   - n == height.length
#   - 2 <= n <= 10^5
#   - 0 <= height[i] <= 10^4

# ------------------------------------------------------------
# APPROACH — Two Pointers
# ------------------------------------------------------------
# Start with left at 0 and right at the last index.
# At every step:
#   - Calculate width = right - left (indices, not values)
#   - Calculate height = min(height[left], height[right])
#   - area = width × height
#   - Update max_water if area is bigger
#   - Move the shorter wall inward (it's the limiting factor)
#     if height[left] > height[right] → move right inward
#     else → move left inward
#
# Why move the shorter wall?
# The shorter wall limits the area — keeping it and reducing
# width can only make things worse. Moving it gives a chance
# at a taller wall and potentially more area.
#
# Time Complexity  : O(n) — single pass, two pointers
# Space Complexity : O(1) — only a few variables used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            width = right - left
            heights = min(height[left], height[right])
            area = width * heights

            if area > water:
                water = area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return water


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # Expected: 49
print(s.maxArea([1, 1]))                           # Expected: 1
print(s.maxArea([4, 3, 2, 1, 4]))                 # Expected: 16
print(s.maxArea([1, 2, 1]))                        # Expected: 2

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Water fills up to the shorter wall — shorter wall limits the area
# - width = right index - left index (indices, not values)
# - height = min(height[left], height[right]) (values, not indices)
# - Always move the shorter wall inward — keeping it only reduces width
# - Two pointers moving independently → always use while loop not for loop
# - One pass from both ends inward covers all useful combinations