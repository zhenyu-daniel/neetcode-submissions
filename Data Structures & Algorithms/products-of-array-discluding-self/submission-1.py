class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*(len(nums))
        pos = [1]*(len(nums))
        n = len(nums)
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            pos[i] = pos[i+1] * nums[i+1]

        return [pre[i] * pos[i] for i in range(n)]
