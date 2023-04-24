# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [i for i in itertools.combinations(range(1, n+1), k)]
