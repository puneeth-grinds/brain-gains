# ============================================================
# PLUS ONE
# Difficulty: Easy
# Link: https://leetcode.com/problems/plus-one/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# Given a large integer represented as an array digits where
# each digits[i] is the ith digit of the integer (ordered most
# significant to least significant), increment the integer by
# one and return the resulting array.
#
# Example 1:
#   Input:  digits = [1, 2, 3]
#   Output: [1, 2, 4]
#   Reason: 123 + 1 = 124
#
# Example 2:
#   Input:  digits = [4, 3, 2, 1]
#   Output: [4, 3, 2, 2]
#   Reason: 4321 + 1 = 4322
#
# Example 3:
#   Input:  digits = [9]
#   Output: [1, 0]
#   Reason: 9 + 1 = 10
#
# Constraints:
#   - 1 <= digits.length <= 100
#   - 0 <= digits[i] <= 9
#   - digits does not contain leading zeros

# ------------------------------------------------------------
# APPROACH — Loop From Back With Carry
# ------------------------------------------------------------
# Addition always starts from the least significant digit (rightmost).
# Walk from back to front handling three cases naturally:
#
# Case 1 → digit is not 9
#           add 1 to it, return immediately — no carry needed
#
# Case 2 → digit is 9, carry bubbles left
#           set digit to 0, loop continues left naturally
#
# Case 3 → all digits were 9
#           loop finishes, all set to 0, insert 1 at the front
#
# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — modified in place (O(n) only for all-9s case)

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # all digits were 9 — carry goes beyond index 0
        digits.insert(0, 1)
        return digits


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.plusOne([1, 2, 3]))      # Expected: [1, 2, 4]
print(s.plusOne([4, 3, 2, 1]))   # Expected: [4, 3, 2, 2]
print(s.plusOne([9]))            # Expected: [1, 0]
print(s.plusOne([9, 9, 9]))      # Expected: [1, 0, 0, 0]
print(s.plusOne([1, 9, 9]))      # Expected: [2, 0, 0]

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Most significant = leftmost digit, least significant = rightmost
# - Always start addition from the rightmost digit — like hand addition
# - If digit is 9 → set to 0 and let the loop carry left naturally
# - Don't manually touch digits[i-1] in the else block — loop handles it
# - If loop finishes, all digits were 9 — insert 1 at front
# - digits.insert(0, 1) places 1 at index 0, shifting everything right