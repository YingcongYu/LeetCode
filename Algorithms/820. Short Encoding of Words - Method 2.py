# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        counter = Counter(word[i:] for word in words for i in range(len(word)))
        return sum(len(word)+1 for word in words if counter[word] == 1)
