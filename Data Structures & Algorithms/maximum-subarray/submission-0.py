class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cum_sum = 0
        for i in nums:
            if cum_sum < 0:
                cum_sum = 0
            
            cum_sum += i
            max_sum = max(max_sum, cum_sum)
        return max_sum

