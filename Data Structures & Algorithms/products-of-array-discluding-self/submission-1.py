class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Brute force
        1. double loop at each i compute prodcut with every other i
        2. this is inefficent and results in O(n^2)
        Optimal approach: we can precompute the product of eveyr element to the left(the prefix) and every elemnt to th erht(the suffix of each number). Then to get th eproduct at i it is simplt prefix[i] * suffix[i] when computing prefix and suffix we exclude i itself. we make the prefix of idex 0 1, and the suffix of index n-1 1. hence result[i]= prefix[i] * suffix[i]. orefix[i] = prefix[i-1] * nums[i-1]. suffix[i] = suffix[I+1} * nums{i+1]}]"""
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        result = [0] * len(nums)
        prefix[0] = 1
        suffix[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1] * nums[j+1]
        for k in range(len(nums)):
            result[k] = prefix[k] * suffix[k]
        
        return result

        


