class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        longest = 0 


        # check odd 
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r]) > longest:
                res = s[l+1:r]
                longest = len(s[l+1:r])






        # check even
        for i in range(len(s)):
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r]) > longest:
                res = s[l+1:r]
                longest = len(s[l+1:r])


        return res
