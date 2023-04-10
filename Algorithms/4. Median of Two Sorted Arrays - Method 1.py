# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid1_pos = math.floor((len(nums1)+len(nums2)+1)/2)
        mid2_pos = math.ceil((len(nums1)+len(nums2)+1)/2)
        mid1 = 0
        mid2 = 0
        m = 0
        n = 0
        while (mid1_pos > 0 or mid2_pos > 0) and (m < len(nums1) and n < len(nums2)):
            mid1_pos -= 1
            mid2_pos -= 1
            if nums1[m] <= nums2[n]:
                if mid1_pos == 0:
                    mid1 = nums1[m]
                if mid2_pos == 0:
                    mid2 = nums1[m]
                m += 1
            else:
                if mid1_pos == 0:
                    mid1 = nums2[n]
                if mid2_pos == 0:
                    mid2 = nums2[n]
                n += 1
        while (mid1_pos > 0 or mid2_pos > 0) and m < len(nums1):
            mid1_pos -= 1
            mid2_pos -= 1
            if mid1_pos == 0:
                mid1 = nums1[m]
            if mid2_pos == 0:
                mid2 = nums1[m]
            m += 1
        while (mid1_pos > 0 or mid2_pos > 0) and n < len(nums2):
            mid1_pos -= 1
            mid2_pos -= 1
            if mid1_pos == 0:
                mid1 = nums2[n]
            if mid2_pos == 0:
                mid2 = nums2[n]
            n += 1
        return (mid1+mid2) / 2
