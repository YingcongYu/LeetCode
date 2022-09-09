# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1 and not prerequisites:
            return [0]
        
        dic = {}
        for i in prerequisites:
            if i[0] in dic:
                dic[i[0]].append(i[1])
            else:
                dic[i[0]] = [i[1]]
        
        output = []
        ready = [x for x in range(numCourses) if x not in dic.keys()]

        while ready:
            node = ready.pop()
            output.append(node)
            for i in dic:
                if node in dic[i]:
                    dic[i].remove(node)
                    if not dic[i]:
                        ready.append(i)
                    
        if len(output) != numCourses:
            return []

        return output
