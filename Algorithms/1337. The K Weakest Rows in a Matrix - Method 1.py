# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_soldiers = []
        for i, row in enumerate(mat):
            num_soldiers.append((i, sum(row)))
        
        num_soldiers.sort(key = lambda x: (x[1], x[0]))

        return [num_soldiers[x][0] for x in range(k)]
