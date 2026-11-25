class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = dict()
        for st in strs:
            key = set()
            for s in st:
                key.add(s)
            key = "".join(sorted(list(key)))
            keys[key] = keys.get(key, []) + [st]

        return list(keys.values())
        