class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slow = 0

        for fast in range(0, len(s)):
            # print(s[slow:fast+1])
            if s[slow:fast+1] in wordDict:
                slow = fast+1
        
        return slow >= len(s)
        