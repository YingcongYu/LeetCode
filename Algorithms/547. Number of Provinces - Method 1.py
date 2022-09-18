# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connect = defaultdict(list)
        visited = [False for _ in range(len(isConnected))]
        output = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    connect[i].append(j)
                    
        def visit(city):
            visited[city] = True
            for i in connect[city]:
                if not visited[i]:
                    visit(i)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                visit(i)
                output += 1
                
        return output
