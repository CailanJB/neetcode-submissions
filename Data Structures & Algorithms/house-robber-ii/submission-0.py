class Solution:
    def rob(self, nums: List[int]) -> int:
        """Similar to house robber 1 insstead since this is ciruclar this means the first and last house are neighbors. This means both of the houses cannot possibly be in the optimal solution since that would break the constraint that we can't rob both adjacent houses.
        
        Hence the otpimal profit would be including house 1 so the profit if decide to rob houses 1 to n-2. Or deciding to not use house and we decide to rob houses 2 to n-1
        Hence we just run the dp algorithm for both caes and take the max between the profits.
        optimal_profit = max(rob(nums[:n],rob(1:n+1))"""

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        
        return max(self.rob_helper(nums[:-1]),self.rob_helper(nums[1:]))
    
    def rob_helper(self,nums):
        if len(nums) == 0: return 0
        if len(nums)==1:
            return nums[0]
        dp = [0] * len(nums)
        #base casees
        dp[0] = nums[0] #robbing the 1st house would give us profit nums[0]
        dp[1] = max(nums[0],nums[1]) #robbing the first two houses the max is either biggest price between the 1st and 2nd house

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]

        
        