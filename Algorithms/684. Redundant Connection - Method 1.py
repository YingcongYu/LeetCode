# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = [x for x in range(len(edges)+1)]
        
        def find(edge):
            if visited[edge] != edge:
                return find(visited[edge])
            return edge
        
        for a, b in edges:
            source_a = find(a)
            source_b = find(b)
            if source_a != source_b:
                visited[source_b] = source_a
            else:
                return [a,b]
