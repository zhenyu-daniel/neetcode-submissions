class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            temp = ''.join(sorted(word))
            if temp in hash_map:
                hash_map[temp].append(word)
            else:
                hash_map[temp] = [word]

        res = list(hash_map.values())
        return res