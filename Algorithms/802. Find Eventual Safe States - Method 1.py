# There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
# meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. 
# A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False] * len(graph)
        ref = [False] * len(graph)

        flag = 1
        while flag > 0:
            flag = 0
            for index, go_to in enumerate(graph):
                if not ref[index] and (len(go_to) == 0 or all(ref[x] for x in go_to)):
                    safe[index] = True
                    flag += 1
                    ref[index] = True
        
        return [x for x in range(len(safe)) if safe[x] == True]
