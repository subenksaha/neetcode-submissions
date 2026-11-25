class Solution:
    def numDecodings(self, s: str) -> int:
        def recursion(pos):
            if pos >= len(s): return 0
            first = s[pos:pos+1]
            second = s[pos:pos+2]
            count = 0
            if first  == "0":
                count = 0
            elif 1 <= int(first) <= 10 and 10 <= int(second) <= 26:
                count = 2
            else: 
                count = 1
            print(count)
            return count + recursion(pos + 2)
        return recursion(0)