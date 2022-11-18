# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        reference = [[] for x in range(target+1)]
        
        for i in range(target+1):
            if i == 0:
                for num in candidates:
                    if num + i <= target:
                        reference[num+i].append([num])
            elif reference[i]:
                for num in candidates:
                    if num + i <= target:
                        for combination in reference[i]:
                            temp = combination+[num]
                            mark = 0
                            for existing in reference[num+i]:
                                if Counter(temp) == Counter(existing):
                                    mark = 1
                                    break
                            if mark != 1:
                                reference[num+i].append(temp)
        
        return reference[target]