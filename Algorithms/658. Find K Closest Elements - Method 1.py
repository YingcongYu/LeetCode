# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(x)
        arr.sort()
        front = arr.index(x) - 1
        back = arr.index(x) + 1
        output = []
        while k > 0:
            if front < 0:
                output.append(arr[back])
                back += 1
            elif back == len(arr):
                output.append(arr[front])
                front -= 1
            elif x - arr[front] <= arr[back] - x:
                output.append(arr[front])
                front -= 1
            else:
                output.append(arr[back])
                back += 1
            k -= 1
        return sorted(output)
