class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        
        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
                if hash_map[char]<0:
                    return False
            else:
                return False

        total = sum(list(hash_map.values()))
        print(hash_map)
        if total == 0:
            return True
        else:
            return False