from collections import Counter
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """An anagram needs two conditions.
        1. both strings are the same length
        2. the count for each letter in string 1 and string 2 match.
        3. if both these conditions are correct this is a anagram
        4. use a map to store the cout of the letters for each string """
        
        count1 = dict()
        count2 = dict()

        for char in s:
            count1[char] = count1.get(char,0) + 1
        
        for char in t:
            count2[char] = count2.get(char,0) + 1
        
        return count1 == count2 
        