from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        incoming = []

        for i, (enq, process) in enumerate(tasks):
            heappush(incoming, (enq, process, i))

        available = []
        res = []
        time = 0

        while incoming or available:

            # Move all available tasks into the processing heap
            while incoming and incoming[0][0] <= time:
                enq, process, index = heappop(incoming)
                heappush(available, (process, index))

            # If no task is available, jump to the next enqueue time
            if not available:
                time = incoming[0][0]
                continue

            # Execute the task with shortest processing time
            process, index = heappop(available)

            time += process
            res.append(index)

        return res