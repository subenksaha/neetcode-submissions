class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = dict()
        for st in strs:
            key = list()
            for s in st:
                key.append(s)
            key = "".join(sorted(key))
            keys[key] = keys.get(key, []) + [st]

        return list(keys.values())
        