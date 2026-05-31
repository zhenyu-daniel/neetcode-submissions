class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]*n

        def dfs(i):
            if i >= n:
                return i == n
            if res[i] != 0:
                return res[i]
            res[i] = dfs(i+1) + dfs(i+2)
            return res[i]

        return dfs(0)