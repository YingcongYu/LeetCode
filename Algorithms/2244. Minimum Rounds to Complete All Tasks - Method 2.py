# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. 
# In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)
        output = 0
        for i in count:
            if count[i] > 4:
                if count[i] % 3 != 0:
                    output += 1
                output += count[i] // 3
            else:
                if count[i] == 1:
                    return -1
                elif count[i] == 3:
                    output += 1
                else:
                    output += count[i] // 2
        return output
