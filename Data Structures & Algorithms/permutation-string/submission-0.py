class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sorted then using two pointer
        def create_map(s):
            hash_map = {}

            for i in s:
                if i in hash_map:
                    hash_map[i] += 1
                else:
                    hash_map[i] = 1

            return hash_map

        set_1 = create_map(s1)

        l, r = 0, len(s1)

        while r <= len(s2):
            temp = create_map(s2[l:r])
            if temp == set_1:
                return True
            else:
                l += 1
                r += 1

        return False



