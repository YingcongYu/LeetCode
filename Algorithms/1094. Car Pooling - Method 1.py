# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers 
# and the locations to pick them up and drop them off are fromi and toi respectively. 
# The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])
        current = 0
        heap = []
        
        for i in trips:
            while heap and heap[0][0] <= i[1]:
                current -= heapq.heappop(heap)[1]
            heapq.heappush(heap, [i[2], i[0]])
            current += i[0]
            if current > capacity:
                return False
        return True
