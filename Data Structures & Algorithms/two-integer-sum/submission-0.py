class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution 1
        hash_map = {}

        for idx, val in enumerate(nums):
            temp = target - val
            if val not in hash_map:
                hash_map[temp] = idx
            else:
                res = [hash_map[val], idx]
                return res