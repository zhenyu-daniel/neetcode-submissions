import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        pre_product = []
        for i in range(len(nums)):
            if i == 0:
                pre_product.append(1)
            else:
                temp = math.prod(nums[:i])
                pre_product.append(temp)

        post_product = []
        for i in range(len(nums)):
            if i == len(nums):
                post_product.append(1)
            else:
                temp = math.prod(nums[i+1:])
                post_product.append(temp)

        for i in range(len(pre_product)):
            res.append(pre_product[i]*post_product[i])

        return res