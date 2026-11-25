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
        return values[-1][1] if ind >= len(values) else values[ind][1]
        
