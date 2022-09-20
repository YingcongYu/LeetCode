# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        output = 0
        
        for i in s:
            count = temp.find(i)
            if count != -1:
                output = max(output, len(temp))
                temp = temp[count+1:]
            temp += i
            
        return max(output, len(temp))
