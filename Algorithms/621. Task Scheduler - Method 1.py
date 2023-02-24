# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
# that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        times = 0
        not_done = Counter(tasks)
        n += 1

        while not_done:
            ready = not_done.most_common(n)
            for i, _ in ready:
                if not_done[i] > 1:
                    not_done[i] -= 1
                else:
                    del not_done[i]
            times += len(ready)
            if not_done:
                times += n - len(ready)
        
        return times
