class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """For each index we can calculate the sum of all the values to its left, and calculate the sum of the all th evalus to its right and store the result. This would take O(n^2) time since we are doing repeated sub arrays.
        Instead we can use a prefix sum array that does this in one pass and a suffix sum array then after forming those arrays we go pair and at any index if the prefix sum equals the suffix sum that is oyr left most pviot. If we dont find one return -1 """

        if len(nums)==0: return -1
        if len(nums) == 1: return 0
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
       
        #build prefix array
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        #build suffix array: we start at the 2nd to last index and work our way to the front. we stop at -1 since we need to add suffix[0]
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1] + nums[j]
        
        for k in range(n):
            if prefix[k] == suffix[k]:
                return k
        
        return -1
        