class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1
        temp = ''
        for i in s:
            if i.isalnum():
                temp += i.lower()
        return temp == temp[::-1]
