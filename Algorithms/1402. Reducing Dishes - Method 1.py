# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level 
# i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        positive_start = 0
        all_cur_nums = 0
        cur_multiply = 1
        output = 0
        for i, n in enumerate(satisfaction):
            if cur_multiply == 1:
                positive_start = i
            if n >= 0:
                all_cur_nums += n
                output += cur_multiply * n
                cur_multiply += 1
        
        for i in range(positive_start-1, -1, -1):
            if output >= max(output, output+all_cur_nums+satisfaction[i]):
                break
            else:
                output += all_cur_nums + satisfaction[i]
                all_cur_nums += satisfaction[i]
        
        return output
