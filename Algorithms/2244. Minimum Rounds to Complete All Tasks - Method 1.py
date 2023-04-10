# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. 
# In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)
        output = 0
        for i in count:
            while count[i] > 1:
                if count[i] > 4:
                    count[i] -= 3
                else:
                    if count[i] == 3:
                        count[i] -= 3
                    else:
                        count[i] -= 2
                output += 1
            if count[i] == 1:
                return -1
        return output
