class Solution:
    def numDecodings(self, s: str) -> int:
        memo = { len(s): 1 }
        def recursion(pos):
            if pos in memo:
                return memo[pos]
            if s[pos] == "0":
                return 0
            count = recursion(pos+1)
            if pos+1 < len(s):
                if s[pos] in "12" and s[pos+1] in "0123456":
                    count += recursion(pos+2)
            memo[pos] = count
            return count
            


        return recursion(0)