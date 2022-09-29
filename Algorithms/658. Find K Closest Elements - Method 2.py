# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap, (-abs(i - x), -i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while heap:
            output.append(-heap.pop()[1])
        
        return sorted(output)
