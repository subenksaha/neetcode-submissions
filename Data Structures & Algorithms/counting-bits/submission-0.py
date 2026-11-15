class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for t, c in enumerate(list(range(n+1))):
            for i in range(32):
                if c & (1<<i):
                    res[t] += 1
        return res

        