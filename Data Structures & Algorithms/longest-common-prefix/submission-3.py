class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """1. What exactly is a prefix?
        2. When we say longest cmmon prefix does each string have to share the same prefix to some    capacity?
        3. Lets consider the first string to be the longest prefix what we can do is go through each charcter in the inital prefix and see if it matches with all the other strings. if it does then that letter is valid. The moment one of the letetrs dont match that is the end of the preix. The moment we hit a charcter not in the other charcters we now for a fat this is the longets possible prefix because base don our second condition every string must share the same prefix so if string i has letter t then the other strings muts have letter t after and if it doesnt that means the lngets prefix is the previous;"""

        if len(strs) == 0: return ""
        #we can immeditaely return empty string if the our intila prefix str[0] its first letter is not a first letter in any of the words this means there can be no possible prefix.
        initial_prefix = strs[0]
        #for each letter in the intial prefix we need to check that the letter is in the same posiiton for every string in the array.
        for i in range(len(initial_prefix)):
            for s in strs:
                #this means the current prefix is no longer valid/we must make sure we dont go out of bounds either.
                if i >= len(s) or initial_prefix[i] != s[i] :
                    return s[:i]
        
        return strs[0]

        