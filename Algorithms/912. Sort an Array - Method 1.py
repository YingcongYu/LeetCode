# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                mergeSort(left)
                mergeSort(right)

                l = 0
                r = 0
                num_index = 0
                while l < len(left) and r < len(right):
                    if left[l] < right[r]:
                        nums[num_index] = left[l]
                        l += 1
                    else:
                        nums[num_index] = right[r]
                        r += 1
                    num_index += 1
                while l < len(left):
                    nums[num_index] = left[l]
                    l += 1
                    num_index += 1
                while r < len(right):
                    nums[num_index] = right[r]
                    r += 1
                    num_index += 1
        mergeSort(nums)
        return nums
