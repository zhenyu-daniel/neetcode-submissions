class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for each element , there are two choices: add or skip
        dp = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        # dp = [-1]*len(nums)

        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         dp[i] = max(dp[i-1]+1, dp[i-1])
        #     else:
        #         dp[i] = dp[i-1]

        # return max(dp)