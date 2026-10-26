class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:          # sorted, so no way to reach 0
                break
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate first numbers
                continue

            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:   # skip duplicate seconds
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:   # skip duplicate thirds
                        r -= 1
        return res
            