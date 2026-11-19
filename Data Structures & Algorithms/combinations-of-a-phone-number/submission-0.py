class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tbl = {
            "2": ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if not digits: return []
        def recursion(pos, comb):
            if len(comb) == len(digits):
                res.append(comb[:])
                return
            digit = digits[pos]
            for cmb in tbl[digit]:
                recursion(pos+1, comb + cmb)
        recursion(0, "")
        return res