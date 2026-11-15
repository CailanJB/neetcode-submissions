class Solution:
    def rob(self, nums: List[int]) -> int:
        """At each house i we have two possible choices.
        1. We can either rob the house in that case our profit would be the nums[i] + our max profit from the i-2 house since if we choose this house our profit relies on our profit from the 2nd previous house.
        2. We can skip the house in that case our profit would be the profit we had at the previous house.i-1
        3. Hence the recurrence relation is as so. let dp[i] represent the max possible profit we can achive robbing first i+1 housess. 
        dp[0] = 0 since robbing the first house results in a prive of 0.
        dp[1] = max(nums[0],nums[1]). Robbing the first two houses the best profit is either we rob the first house or rob the 2nd house. 
        So at each i our proit would be if we rob the house then we add nums[i] + dp[i-2] since dp[i-2] is the max profit we can from the prvious 2nd house.
        dp[i] = max(dp[i-1],nums[i] + dp[i-2])
        At the end we return dp[-1] because that would be the max profit to rob money from the houses stickng to the contraints."""

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        #base casees
        dp[0] = nums[0] #robbing the 1st house would give us profit nums[0]
        dp[1] = max(nums[0],nums[1]) #robbing the first two houses the max is either biggest price between the 1st and 2nd house

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]



    

        
    
        