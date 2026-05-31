class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = []
        
        if not nums:
            return 0

        for num in nums:
            if num-1 not in nums:
                res.append([num])
                while num+1 in nums:
                    res[-1].append(num+1)
                    num += 1
        
        length = []
        for i in res:
            length.append(len(i))

        return max(length)