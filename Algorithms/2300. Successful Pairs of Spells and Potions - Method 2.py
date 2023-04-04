# You are given two positive integer arrays spells and potions, of length n and m respectively, 
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        spl = sorted(set(spells))[::-1]
        log = {}
        potion_length = len(potions)
        i = 0
        for s in spl:
            while i < potion_length and s * potions[i] < success:
                i += 1
            if i == potion_length:
                log[s] = 0
            else:
                log[s] = potion_length - i
        return [log[s] for s in spells]
