from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for name in strs:
            count = [0]*26
            for c in name:
                count[ord(c)-ord("a")]+=1
            freq[tuple(count)].append(name)
        return list(freq.values())
            
                

        