class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        longest = 0 


        # check odd 
        for i in range(len(s)):
            l = r = i
            while r <= len(s)-1 and l>= 0 and s[r] == s[l] :
                if len(s[l:r+1]) > longest:
                    longest = len(s[l:r+1])
                    res = s[l:r+1]
                r += 1
                l -=1


        # check even
        for i in range(len(s)-1):
            l = i
            r = i+1
            while r <= len(s)-1 and l>=0 and s[r] == s[l]:
                if len(s[l:r+1]) > longest:
                    longest = len(s[l:r+1])
                    res = s[l:r+1]
                r += 1
                l -=1 
                

        return res
