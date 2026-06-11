class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in s:
            if i == "(":
                res.append(")")
            elif i == "{":
                res.append("}")
            elif i == "[":
                res.append("]")
            else:
                if not res or res.pop() != i:
                    return False
                
        if len(res) == 0:
            return True
        else:
            return False