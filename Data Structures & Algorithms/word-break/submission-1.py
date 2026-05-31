class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(sub):
            if sub == "":
                return True

            if sub in memo:
                return memo[sub]

            for word in wordDict:
                if sub.startswith(word):
                    if dfs(sub[len(word):]):
                        memo[sub] = True
                        return True

            memo[sub] = False
            return False

        return dfs(s)