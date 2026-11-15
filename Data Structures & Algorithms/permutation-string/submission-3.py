class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = collections.Counter(s1)
        ttl_len = len(s1)
        slow, fast = 0, 0

        while fast < len(s2):

            while fast < len(s2) and s2[fast] in freq and freq[s2[fast]] > 0:
                freq[s2[fast]] -= 1
                ttl_len -= 1
                fast += 1
                if ttl_len == 0:
                    return True
            slow += 1
            fast = slow
            freq = collections.Counter(s1)
            ttl_len = len(s1)

        return False