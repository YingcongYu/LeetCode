# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        front = 0
        end = len(s) - 1
        output = list(s)
        while front < end:
            if output[front] in vowels and output[end] in vowels:
                output[front], output[end] = output[end], output[front]
                front += 1
                end -= 1
            if output[front] not in vowels:
                front += 1
            if output[end] not in vowels:
                end -= 1
        return ''.join(output)
