from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = {
            'a': a,
            'b': b,
            'c': c
        }
        heap = []
        for char, cnt in freq.items():
            if cnt != 0:
                heappush(heap, (-cnt, char))

        res = ""

        while heap:
            cnt, char = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                cnt2, char2 = heappop(heap)
                res += char2
                cnt2 += 1
                if cnt2 < 0:
                    heappush(heap, (cnt2, char2))
                heappush(heap, (cnt, char))
            else:
                res += char
                cnt += 1
                if cnt < 0:
                    heappush(heap, (cnt, char))
        return res
        