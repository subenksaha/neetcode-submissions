class Solution:
    def numDecodings(self, s: str) -> int:
        def recursion(pos):
            if pos >= len(s):
                return 1
            if s[0] == "0":
                return 0
            count = recursion(pos+1)
            if pos < len(s) - 1:
                if s[pos] in "12" and s[pos+1] in "0123456":
                    count += recursion(pos+2)
            return count
            


        return recursion(0)