# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append((value, timestamp))
        else:
            self.values[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        try:
            temp = self.values[key]
            front = 0
            end = len(temp) - 1
            
            while front < end:
                mid = (front + end) // 2
                if temp[mid][1] == timestamp:
                    return temp[mid][0]
                elif temp[mid][1] > timestamp:
                    if temp[mid-1][1] < timestamp:
                        return temp[mid-1][0]
                    end = mid - 1
                else:
                    if temp[mid+1][1] > timestamp:
                        return temp[mid][0]
                    front = mid + 1
            
            if temp[front][1] > timestamp:
                return ''
            else:
                return temp[front][0]
        except:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
