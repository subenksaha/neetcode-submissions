from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        ind = bisect.bisect_left(values, timestamp, key=lambda x: x[0])
        ind = min(ind, len(values)-1)
        if values[ind][0] <= timestamp:
            return values[ind][1]
        return ""
        
