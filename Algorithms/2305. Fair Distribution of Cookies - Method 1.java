// You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. 
//   You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. 
//   All the cookies in the same bag must go to the same child and cannot be split up.

// The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

// Return the minimum unfairness of all distributions.


class Solution {
    public int distributeCookies(int[] cookies, int k) {
        int[] distribution = new int[k];
        return dfs(0, cookies, k, distribution, k);
    }

    public int dfs(int cookie, int[] cookies, int k, int[] distribution, int bottomline) {
        if (cookies.length - cookie < bottomline) {
            return Integer.MAX_VALUE;
        }

        if (cookie == cookies.length) {
            int unfairness = 0;
            for (int num_cookies : distribution) {
                unfairness = Math.max(unfairness, num_cookies);
            }
            return unfairness;
        }

        int minimum_unfairness = Integer.MAX_VALUE;
        for (int i = 0; i < k; i++) {
            bottomline -= distribution[i] == 0 ? 1 : 0;
            distribution[i] += cookies[cookie];
            minimum_unfairness = Math.min(minimum_unfairness, dfs(cookie+1, cookies, k, distribution, bottomline));
            distribution[i] -= cookies[cookie];
            bottomline += distribution[i] == 0 ? 1 : 0;
        }

        return minimum_unfairness;
    }
}
