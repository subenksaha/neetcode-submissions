class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        longest = 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                l = r
                seen = set()
            seen.add(s[r])
            longest = max(longest, (r-l+1))
        return longest
        