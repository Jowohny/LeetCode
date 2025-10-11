from collections import defaultdict
class TimeMap:
    #when initializing, we obviously need a dictionary to store key pair values
    #when setting, just use the given key value pairs with an added timestamp to the value
    #when it comes to getting the value, it is ever so slightly more complicated since we have to
    #account for timestamps that don't exist in the dictionary yet
    #iterate from the loop backwards to find the closest timestamp

    def __init__(self):
        self.stamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stamps:
            return ""
        
        timeArray = self.stamps[key]
        roundDown = ""

        for i in range(len(timeArray) - 1, -1, -1):
            if timeArray[i][0] <= timestamp:
                roundDown = timeArray[i][1]
                break
        
        return roundDown

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)