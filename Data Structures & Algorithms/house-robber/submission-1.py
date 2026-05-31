class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for idx, num in enumerate(nums[2:]):
            dp[idx+2] = max(dp[idx+2-2]+num, dp[idx+2-1])

        return max(dp)
