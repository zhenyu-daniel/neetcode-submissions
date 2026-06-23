class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        hash_map= {}
        res = []

        def two_sum(left, right, target):
            pairs = []

            while left < right:
                s = nums[left] + nums[right]

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    pairs.append([left, right])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            return pairs


        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            for l, r in two_sum(i+1, len(nums)-1, target):
                res.append([nums[i], nums[l], nums[r]])

        return res
