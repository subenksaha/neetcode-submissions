class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parents = dict({
            ")" : "(",
            "}" : "{",
            "]" : "["
        })

        for c in s:
            if c not in parents:
                stack.append(c)
            else:
                if not stack: return False
                t = stack.pop()
                if t != parents[c]:
                    return False
        return True

        