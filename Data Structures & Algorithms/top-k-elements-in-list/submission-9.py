class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash table solution
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        times = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            times[cnt].append(num)
            
        res = []
        for i in range(len(times)-1,0,-1):
            for num in times[i]:
                res.append(num)
                if len(res)==k:
                    return res

            
