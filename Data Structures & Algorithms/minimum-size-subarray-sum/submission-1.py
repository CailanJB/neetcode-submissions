class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Slidng windowwe move ghe right pointer and we move th elft pointr in when the sum goes over target
        left = 0
        cur_sum = 0
        cur_dist = 0
        min_dist = float("inf")
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while cur_sum >= target:
                cur_dist = (right-left) + 1
                min_dist = min(min_dist,cur_dist)
                cur_sum-=nums[left]
                left+=1
                
        
        return 0 if min_dist == float("inf") else min_dist
            
           

            
        