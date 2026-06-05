class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        v = (r-l)* min(heights[l], heights[r])

        while l<r:
            if heights[l] < heights[r]:
                l += 1
                v = max(v,(r-l)* min(heights[l], heights[r]))
            else:
                r -= 1
                v = max(v, (r-l)* min(heights[l], heights[r]))

        return v