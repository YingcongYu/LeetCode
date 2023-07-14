# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.
#   For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = {}
        for course, need in prerequisites:
            try:
                requirements[course].append(need)
            except:
                requirements[course] = [need]

        finished = [False] * numCourses

        def take(num, visited):
            if visited[num] == True:
                return False

            if finished[num] == True:
                return True
            
            visited[num] = True
            output = True
            try:
                for i in requirements[num]:
                    if finished[i] == False:
                        output = all([output, take(i,visited)])
            except:
                pass
        
            finished[num] = True
            return output
        
        return all([take(x, [False]*numCourses) for x in range(numCourses)])
