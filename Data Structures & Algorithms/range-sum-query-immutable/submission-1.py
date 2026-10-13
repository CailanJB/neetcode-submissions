class NumArray:

    def __init__(self, nums: List[int]):
        """We first construct the prefix sum array"""
        self.prefix = []
        cur = 0
        for num in nums:
            cur+=num
            self.prefix.append(cur)
        #each index in the prefix array corresponds to the sum of all the elements before and at that index 
        #ex for nms = [1,2] prefix[0] = 1 and prefix[1] = 3 = prefix[i-1] + nums[i]
       
        

    def sumRange(self, left: int, right: int) -> int:
        """Brute firce just: compute the sum from left to right.O(N) time for each query
        optimal approach prefix sum: Getting the sum of the values befoe index 
        now that we cnstrcted th eprefix sum array to get the sum of the elements between left and right.
        Since we have the prefix of left, sum of numbers before left and we have the prefix of right: the sum of the numbers before right. the sum of the values bwteen left and riht would just be prefix[right]-prefix[left]"""
        if left > 0:
            return self.prefix[right] - self.prefix[left-1]
        else:
            return self.prefix[right]
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)