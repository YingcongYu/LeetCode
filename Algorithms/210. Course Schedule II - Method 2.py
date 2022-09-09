# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {x:set() for x in range(numCourses)}
        
        dic = collections.defaultdict(set)
        for i, j in prerequisites:
            prereq[i].add(j)
            dic[j].add(i)
        
        output = []
        ready = [x for x, y in prereq.items() if len(y) == 0]

        while ready:
            course = ready.pop()
            output.append(course)
            
            if len(output) == numCourses:
                return output
            
            for i in dic[course]:
                prereq[i].remove(course)
                if not prereq[i]:
                    ready.append(i)
        return []
