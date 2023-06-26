// You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

// You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
// You will run k sessions and hire exactly one worker in each session.
// In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
// For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
// In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
// If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
// A worker can only be chosen once.

// Return the total cost to hire exactly k workers.


class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> left_pq = new PriorityQueue<>();
        PriorityQueue<Integer> right_pq = new PriorityQueue<>();
        for (int i = 0; i < candidates; i++) {
            left_pq.add(costs[i]);
        }
        for (int i = Math.max(candidates, costs.length-candidates); i < costs.length; i++) {
            right_pq.add(costs[i]);
        }

        long output = 0;
        int left = candidates;
        int right = costs.length - candidates - 1;
        for (int i = 0; i < k; i++) {
            if (right_pq.isEmpty() || (!left_pq.isEmpty() && left_pq.peek() <= right_pq.peek())) {
                output += left_pq.poll();
                if (left <= right) {
                    left_pq.add(costs[left]);
                    left += 1;
                }
            }
            else {
                output += right_pq.poll();
                if (left <= right) {
                    right_pq.add(costs[right]);
                    right -= 1;
                }
            }
        }

        return output;
    }
}
