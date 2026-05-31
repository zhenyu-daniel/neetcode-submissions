class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            l = idx + 1
            r = len(nums) - 1
            two_sum = 0 - num
            while l<r:
                temp_sum = nums[l] + nums[r]
                if temp_sum > two_sum:
                    r -= 1
                elif temp_sum < two_sum:
                    l += 1
                else:
                    if [num, nums[l], nums[r]] not in res:
                        res.append([num, nums[l], nums[r]])
                    r -=1
                    l+=1

        return res
