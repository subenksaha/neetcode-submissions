class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) +1
        
        kvs = []
        for key in counter:
            kvs.append([counter.get(key), key])
        kvs = sorted(kvs, reverse=True)
        return list(map(lambda x: x[1], kvs[:k]))