# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ref = {}
        for i in range(n):
            ref[i] = 0
        
        for i, n in edges:
            ref[n] += 1
        
        output = []
        for i in ref:
            if ref[i] == 0:
                output.append(i)
        
        return output
