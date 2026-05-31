class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, num in enumerate(nums):
            if num not in hash_map:
                hash_map[target-num] = idx
            else:
                return [hash_map[num], idx]