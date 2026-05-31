class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1
        # temp = ''
        # for i in s:
        #     if i.isalnum():
        #         temp += i.lower()
        # return temp == temp[::-1]

        # solution 2
        l = 0
        r = len(s) -1

        while l<r:
            while l<r and s[l].isalnum()==False:
                l += 1
            while r>l and s[r].isalnum()==False:
                r -=1    

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1


        return True

