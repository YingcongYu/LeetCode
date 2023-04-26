# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. 
# garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. 
# Picking up one unit of any type of garbage takes 1 minute.

# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

# There are three garbage trucks in the city, each responsible for picking up one type of garbage. 
# Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

# Return the minimum number of minutes needed to pick up all the garbage.


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m_end = 0
        g_end = 0
        p_end = 0
        for i in range(len(garbage)-1, -1, -1):
            if m_end == 0 and 'M' in garbage[i]:
                m_end = i
            if g_end == 0 and 'G' in garbage[i]:
                g_end = i
            if p_end == 0 and 'P' in garbage[i]:
                p_end = i
            if m_end != 0 and g_end != 0 and p_end != 0:
                break
        
        return sum(travel[:m_end]) + sum(travel[:g_end]) + sum(travel[:p_end]) + len(''.join(garbage))
