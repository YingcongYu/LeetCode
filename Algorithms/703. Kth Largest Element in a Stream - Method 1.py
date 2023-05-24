# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.k = k
        self.nums = nums[:k]

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
        elif len(self.nums) < self.k:
            length = len(self.nums)
            for i in range(length):
                if val > self.nums[i]:
                    self.nums.insert(i, val)
            if length == len(self.nums):
                self.nums.append(val)
        elif val > self.nums[-1]:
            for i in range(self.k):
                if val > self.nums[i]:
                    self.nums.insert(i, val)
                    self.nums.pop()
                    break
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
