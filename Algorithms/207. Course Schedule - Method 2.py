# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
# you must take course bi first if you want to take course ai.
#   For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reverse = [[] for _ in range(numCourses)]
        for course, need in prerequisites:
            reverse[need].append(course)

        visited = [0] * numCourses
        def is_cycle(course):
            if visited[course] == -1:
                return True
            if visited[course] == 1:
                return False
            
            visited[course] = -1
            for i in reverse[course]:
                if is_cycle(i):
                    return True
            visited[course] = 1

            return False
        
        for i in range(numCourses):
            if is_cycle(i):
                return False
        
        return True
