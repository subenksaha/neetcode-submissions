class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slow = 0

        for fast in range(1, len(s)):
            if s[slow:fast+1] in wordDict:
                slow = fast+1
        
        return slow == len(s)
        