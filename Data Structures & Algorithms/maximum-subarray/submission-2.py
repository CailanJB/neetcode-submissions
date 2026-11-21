class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Brute force use a double loop to try every subarray to find largest sum.
        instead of recommputing eveyr sub array we can use a sliding window. We move the right pointer and add values and we decrement the left pointer if the sum is negative. that is because adding moree to a negative sum wont give us the largest value. When the sum becomes negative we just set the running sum to 0 then restart thje calculation."""
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum+=num
            max_sum = max(max_sum,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
                
        return max_sum
        
        
        

        