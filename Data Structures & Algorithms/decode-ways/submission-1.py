class Solution:
    def numDecodings(self, s: str) -> int:
        def recursion(pos):
            if pos >= len(s) or s[0] == "0": return 0
            count = 0
            if 10 <= int(s[pos: pos+2]) <= 26:
                count = 2
            if 1 <= int(s[pos]) <= 10:
                count = 1

            return count + recursion(pos+1)
            


        return recursion(0)