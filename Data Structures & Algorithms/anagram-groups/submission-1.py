class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """We get the frequency of the each letter for each strings and store that as a key. we can represent the key as a 26 chacter array tuple. ord(a) - ord(letter). We iterate through each word and get its frequency array. we then check if that frequency array already exist we append the wod to that array. In the end we just return the values"""
        if len(strs) == 0:
            return [[""]]
        
        freq = collections.defaultdict(list)
        for word in strs:
            freq_array = [0] * 26
            for letter in word:
                freq_array[ord(letter)-ord('a')]+=1
            freq[tuple(freq_array)].append(word)
        
        return list(freq.values())


        
        
        