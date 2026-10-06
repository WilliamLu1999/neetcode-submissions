class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in range(0,len(nums)):
            if nums[n] in hashmap:
                hashmap[nums[n]]+=1
            else:
                hashmap[nums[n]] = 1

        s = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        # print(s)
        return list(s.keys())[:k]