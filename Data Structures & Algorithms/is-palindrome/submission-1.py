class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl, fa = 0, len(s)-1
        whitelist = "abcdefghijklmnopqrstuvwxyz0123456789"
        while sl < fa:
            while s[sl].lower() not in whitelist:
                sl += 1
            while s[fa].lower() not in whitelist:
                fa -= 1
            if s[sl].lower() != s[fa].lower():
                return False
            sl += 1
            fa -= 1
        return True
        