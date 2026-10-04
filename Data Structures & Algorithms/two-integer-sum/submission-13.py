class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            else:
                hashmap[nums[i]]=i
        # for i in range(0, len(nums)):
        #     if target-nums[i] not in hashmap: 不能先写这个
        #         hashmap[target-nums[i]]=i
        #     else:
        #         output.append(hashmap[target-nums[i]])
        #         output.append(i)
        #         return sorted(output)
        # {"5":"0"} key 存 unique才行，要不然【5，5】就不work
        # for i in range(0,len(nums)):
        #     hash_map[i]=nums[i]
        #     if target-nums[i] in hash_map.values():
        #         output.append()
        

        # [5,5]

        # 5


        # for n in nums:
        #     if target-n in nums:
        #         output.append(hashmap[n])
        #         output.append(hashmap[target-n])
        #     return sorted(output)