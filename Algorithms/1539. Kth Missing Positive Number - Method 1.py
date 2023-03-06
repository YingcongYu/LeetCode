# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pre = 1
        for i in arr:
            if i - pre < k:
                k -= i - pre
            else:
                return pre + k - 1
            pre = i + 1
        return pre + k - 1
