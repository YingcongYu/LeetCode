# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for i in nums:
            flag = 0
            for j in output:
                if i not in j:
                    j.append(i)
                    flag = 1
                    break
            if flag == 0:
                output.append([i])
        
        return output
