# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def pick(cur, k, path):
            if k == 0:
                output.append(path)
                return
            for i in range(cur, n+1):
                pick(i+1, k-1, path+[i])
        
        pick(1, k, [])
        return output
