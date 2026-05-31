class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for char in strs:
            temp = ''.join(sorted(char))
            if temp in hash_map:
                hash_map[temp].append(char)
            else:
                hash_map[temp] = [char]

        res = list(hash_map.values())

        return res