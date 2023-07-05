// Given an integer array nums where every element appears three times except for one, which appears exactly once. 
//   Find the single element and return it.

// You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            if (counts.containsKey(num)) {
                counts.put(num, counts.get(num)+1);
            }
            else {
                counts.put(num, 1);
            }
        }

        int output = 0;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() == 1) {
                output = entry.getKey();
                break;
            }
        }

        return output;
    }
}
