# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        for i, n in Counter(ransomNote).items():
            if i not in mag:
                return False
            elif n > mag.get(i):
                return False
        return True
