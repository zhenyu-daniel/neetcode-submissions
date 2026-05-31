class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i > len(nums)-1:
                return
            
            curr.append(nums[i])
            if curr not in res:
                res.append(curr.copy())
            dfs(i+1, curr)

            curr.pop()
            if curr not in res:
                res.append(curr.copy())
            dfs(i+1, curr)

        dfs(0, [])

        return res