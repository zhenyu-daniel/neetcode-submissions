class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sorted = ''.join(sorted(s))
        # t_sorted = ''.join(sorted(t))

        # if s_sorted == t_sorted:
        #     return True
        # else:
        #     return False

        # solution 2:
        s_map = {}
        t_map = {}

        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1

        for val in t:
            if val in t_map:
                t_map[val] += 1
            else:
                t_map[val] = 1
        print(s_map)
        print(t_map)

        if s_map == t_map:
            return True
        else:
            return False
