from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('s')] += 1

            key = tuple(count)
            hash_map[key].append(s)

        
        return list(hash_map.values())
