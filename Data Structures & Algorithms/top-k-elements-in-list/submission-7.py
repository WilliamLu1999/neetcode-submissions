class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        arr = []
        for h, v in hashmap.items():
            arr.append([v,h])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res