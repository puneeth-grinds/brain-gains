# ============================================================
# MERGE SORTED ARRAY
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-sorted-array/
# ============================================================

# ------------------------------------------------------------
# PROBLEM STATEMENT
# ------------------------------------------------------------
# You are given two integer arrays nums1 and nums2, sorted in
# non-decreasing order, and two integers m and n representing
# the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single sorted array stored inside nums1.
# nums1 has length m + n where the last n elements are 0 (empty slots).
#
# Example 1:
#   Input:  nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
#   Output: [1,2,2,3,5,6]
#
# Example 2:
#   Input:  nums1 = [1], m=1, nums2 = [], n=0
#   Output: [1]
#
# Example 3:
#   Input:  nums1 = [0], m=0, nums2 = [1], n=1
#   Output: [1]
#
# Constraints:
#   - nums1.length == m + n
#   - nums2.length == n
#   - 0 <= m, n <= 200
#   - 1 <= m + n <= 200
#   - -10^9 <= nums1[i], nums2[j] <= 10^9

# ------------------------------------------------------------
# APPROACH — Three Pointers From the Back
# ------------------------------------------------------------
# Working from the front causes overwriting of real elements.
# Instead, fill from the back — place the largest element last.
#
# a   → starts at last real element of nums1 (m-1)
# b   → starts at last element of nums2 (n-1)
# pos → starts at last slot of nums1 (m+n-1)
#
# Compare nums1[a] vs nums2[b] — place the larger at pos.
# Move that pointer and pos back. Repeat.
#
# After main loop — if nums2 still has leftover elements (b >= 0),
# place them all. No need to handle leftover nums1 elements —
# they are already in place.
#
# Time Complexity  : O(m+n) — single pass through both arrays
# Space Complexity : O(1)   — in-place, no extra space used

# ------------------------------------------------------------
# SOLUTION
# ------------------------------------------------------------

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = m - 1
        b = n - 1
        pos = len(nums1) - 1

        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[pos] = nums1[a]
                a -= 1
                pos -= 1
            else:
                nums1[pos] = nums2[b]
                b -= 1
                pos -= 1

        while b >= 0:
            nums1[pos] = nums2[b]
            b -= 1
            pos -= 1

        return nums1


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))   # Expected: [1,2,2,3,5,6]
print(s.merge([1], 1, [], 0))                    # Expected: [1]
print(s.merge([0], 0, [1], 1))                   # Expected: [1]
print(s.merge([2,0], 1, [1], 1))                 # Expected: [1,2]

# ------------------------------------------------------------
# WHAT I LEARNED
# ------------------------------------------------------------
# - Working from the back avoids overwriting real elements in nums1
# - Three pointers: a and b compare, pos places the winner
# - else is non-negotiable — without it, the else block runs
#   even after the if block executes, corrupting the result
# - After the main loop, leftover nums2 elements must be placed
# - Leftover nums1 elements don't need handling — already in place
# - while loop gives full control over when each pointer moves
#   unlike a for loop which auto-increments every iteration