class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p = 1, 1 
        res = nums[0]

        for num in nums:
            if num !=0:
                temp = max_p
                max_p = max(max_p*num, min_p*num, num)
                min_p = min(temp*num, min_p*num, num)
                res = max(res, max_p)
            else:
                res = max(res, 0)
                max_p = min_p = 1
                continue

        return res