class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # count odd
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        # count even
        for j in range(len(s)):
            l, r = j, j+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res