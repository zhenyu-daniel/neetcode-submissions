class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash_map = {}
        # for i in nums:
        #     if i in hash_map:
        #         return True
        #     else:
        #         hash_map[i] = True
        # return False

        # solution 2
        if len(set(nums)) != len(nums):
            return True
        else:
            return False