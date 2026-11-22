class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        m, l, r, f = 0, 0, 0, True

        while l < len(word1) and r < len(word2):
            if f:
                merged += word1[l]
                l += 1
                f = False
            else:
                merged += word2[r]
                r += 1
                f = True

        while l < len(word1):
            merged += word1[l]
            l += 1
        while r < len(word2):
            merged += word2[r]
            r += 1
        return merged
        