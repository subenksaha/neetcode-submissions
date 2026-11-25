class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) +1
        
        kvs = []
        for k in counter:
            kvs.append((k, counter.get(k)))
        kvs = sorted(kvs, reverse=True)
        return list(map(lambda x: x[0], kvs[:k-1]))