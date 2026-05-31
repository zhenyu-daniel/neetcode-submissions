class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'{':'}', '(': ")", '[':']'}
        stack = []

        for i in s:
            if i in hash_map:
                stack.append(hash_map[i])
            else:
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        
        if len(stack) ==0:
            return True
        else:
            return False