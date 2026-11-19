from collections import Counter
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        for task, count in counts.items():
            heappush(heap, (-count, task))

        t = 0
        queue = deque()

        while heap or queue:
            t += 1
            if not heap:
                t = queue[0][0]
            else:
                count, curr = heappop(heap)
                count += 1
                if count:
                    queue.append((t+n, count, curr))
            if queue and queue[0][0] == t:
                _, cnt, tsk = queue.popleft()
                heappush(heap, (cnt, tsk))
        return t