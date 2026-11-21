
from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        available = list(range(n))
        heapify(available)

        occupied = []
        counts = [0] * n

        for start, end in meetings:

            # Release all rooms available by meeting start
            while occupied and occupied[0][0] <= start:
                end_time, room = heappop(occupied)
                heappush(available, room)

            duration = end - start

            if available:
                # Assign smallest available room
                room = heappop(available)
                heappush(occupied, (end, room))

            else:
                # Delay meeting until earliest room becomes free
                available_time, room = heappop(occupied)

                heappush(
                    occupied,
                    (available_time + duration, room)
                )

            counts[room] += 1

        return counts.index(max(counts))
