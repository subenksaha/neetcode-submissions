from heapq import heappush, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickq = []
        dropq = []

        for passenger, frm, to in trips:
            heappush(pickq, (frm,passenger))
            heappush(dropq, (to, passenger))
        
        time = 0
        count = 0

        while pickq or dropq:
            if dropq and dropq[0][0] == time:
                _, psnger = heappop(dropq)
                count -= psnger
            if pickq and pickq[0][0] == time:
                _, psnger = heappop(pickq)
                count += psnger
            if count > capacity:
                return False
            time += 1
        return True