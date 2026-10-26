class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        weight = min(heights[l],heights[r]) * (r-l)
        while l < r:
            if heights[l]<heights[r]:
                l+=1

            elif heights[l]>=heights[r]:
                r-=1
                
            weight = max(weight, (r-l)* min(heights[l],heights[r]))

        return weight

