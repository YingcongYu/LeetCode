# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nums[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        for i in self.nums:
            if i in vec.nums.keys():
                output += self.nums[i] * vec.nums[i]
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
