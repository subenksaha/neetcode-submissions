class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = set()
        set2 = set()
        for c in s:
            set1.add(c)
        for c in t:
            set2.add(c)
        return set1 == set2