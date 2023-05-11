# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        ref = {}
        
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            
            if (i, j) in ref:
                return ref[(i, j)]
            
            if nums1[i] == nums2[j]:
                ref[(i, j)] = dp(i-1, j-1) + 1
            else:
                ref[(i ,j)] = max(dp(i-1, j), dp(i, j-1))
            
            return ref[(i, j)]
        
        return dp(len(nums1)-1, len(nums2)-1)
