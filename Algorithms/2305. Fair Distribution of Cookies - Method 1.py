# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. 
# You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. 
# All the cookies in the same bag must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float("inf")
        distribution = [0] * k

        def dfs(cookie):
            nonlocal min_unfairness, distribution

            if min_unfairness <= max(distribution):
                return
            
            if cookie == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return
            
            for i in range(k):
                distribution[i] += cookies[cookie]
                dfs(cookie+1)
                distribution[i] -= cookies[cookie]
        
        dfs(0)
        return min_unfairness
