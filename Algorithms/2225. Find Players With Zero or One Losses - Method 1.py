# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}

        for winner, loser in matches:
            if winner not in loses:
                loses[winner] = 0
            
            if loser in loses:
                loses[loser] += 1
            else:
                loses[loser] = 1
        
        zero = []
        one = []

        for i in loses:
            if loses[i] == 1:
                one.append(i)
            elif loses[i] == 0:
                zero.append(i)

        return [sorted(zero), sorted(one)]
