// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
//   such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
//   For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

// You must decrease the overall operation steps as much as possible.


class Solution {
    public boolean search(int[] nums, int target) {
        int front = 0;
        int end = nums.length - 1;
        if (nums[front] > target & nums[end] < target) {
            return false;
        }

        while (front <= end) {
            int mid = (front + end) / 2;
            if (nums[mid] == target) {
                return true;
            }

            while (front < mid & nums[front] == nums[mid]) {
                front++;
            }

            if (nums[front] <= nums[mid]) {
                if (nums[front] <= target & target < nums[mid]) {
                    end = mid - 1;
                }
                else {
                    front = mid + 1;
                }
            }
            else {
                if (nums[mid] < target & target <= nums[end]) {
                    front = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }
        }

        return false;
    }
}
