# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        max_length = 0
        indicator = 0
        reference= {}

        for i in words:
            try:
                if i == i[::-1]:
                    reference[i] += 1
                else:
                    reference[i]
            except:
                if i == i[::-1]:
                    reference[i] = 1
                else:
                    reference[i] = 0

        for i in words:
            try:
                if i != i[::-1]:
                    reference[i[::-1]] += 1
            except:
                pass
        
        for i, n in reference.items():
            if n >= 1:
                if i == i[::-1]:
                    if n % 2 == 0:
                        max_length += n*2
                    elif indicator != 1:
                        max_length += n*2
                        indicator = 1
                    else:
                        max_length += (n-1)*2
                else:
                    max_length += min(reference[i], reference[i[::-1]]) * 2
        return max_length
