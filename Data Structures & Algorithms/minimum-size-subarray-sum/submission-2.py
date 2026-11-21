class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Slidng windowwe move the right pointer and we move the left pointrr in when the sum goes over target. we use a hwile loop to keep moving the lft pointer until the cur_sum is no longer bigger than taregt so we can find a smaller window."""



       
        left = cur_sum = 0
        min_window = float("inf")

        for right in range(len(nums)):
            cur_sum+=nums[right]
            while cur_sum >= target:
                min_window = min(min_window,right-left+1)
                cur_sum-=nums[left]
                left+=1
        
        return 0 if min_window == float("inf") else min_window
                
           

            
        