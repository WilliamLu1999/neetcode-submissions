class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1 ,2 ,4, 6]
        # prefix = [1,1,2,8]
        # suffix = [48,24,6,1]
        prefix = [1] * len(nums)
        for n in range(0,len(nums)):
            if n == 0:
                prefix[n] = 1
            else:
                prefix[n] = nums[n-1]*prefix[n-1]
        # print(prefix)
        suffix = [1] * len(nums)
        for n in range(len(nums)-1,-1,-1):
            if n == len(nums)-1:
                suffix[n] = 1
            else:
                suffix[n] = suffix[n+1] * nums[n+1]
        output = [1]*len(prefix)

        for s in range(0,len(prefix)):
            output[s] = prefix[s]*suffix[s]

        return output