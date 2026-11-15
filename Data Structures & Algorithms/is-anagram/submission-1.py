class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = dict()
        set2 = dict()
        for c in s:
            set1[c] = set1.get(c, 0) + 1
        for c in t:
            set2[c] = set2.get(c, 0) + 1
        
        for k in set1:
            t1 = set1.get(k, 0)
            t2 = set2.get(k, 0)
            if t1 != t2:
                return False
            del set2[k]
        
        return False if len(set2) > 0 else True