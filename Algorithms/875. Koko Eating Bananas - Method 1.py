# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        k = max_k

        while min_k <= max_k:
            mid = (min_k + max_k) // 2
            temp_h = 0
            for i in piles:
                temp_h += math.ceil(i/mid)
            
            if temp_h <= h:
                k = mid
                max_k = mid - 1
            else:
                min_k = mid + 1
        
        return k
