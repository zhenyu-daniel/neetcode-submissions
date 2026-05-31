class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0]* len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx, num in enumerate(nums):
            if idx >=2:
                dp[idx] = max(dp[idx-1], nums[idx]+dp[idx-2])

        return max(dp)
