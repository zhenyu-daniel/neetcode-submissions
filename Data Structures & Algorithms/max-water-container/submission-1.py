class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        l, r = 0, len(heights)-1
        water = 0
        while l < r:
            temp = (r-l)*min(heights[l], heights[r])
            water = max(water, temp)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return water