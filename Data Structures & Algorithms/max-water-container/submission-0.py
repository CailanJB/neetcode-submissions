class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Brute Force approach: We compare each bar with every other bar and keep track of the maximum area. 
        Area = min(height[i],height[j]) * (i-j)
        i-j is thw width between both bars and we take the smallest of hheights betweent the two bars to since the smallest height would dictate how much water gets trapped.
        O(n^2)
        Optimal approach: two pointers
        1. We have a pointer on the left at 0, and on the right as len(nums)-1
        2. We get the width of from left to right and the min(height[left],height[right)]) multiply it and store the result.
        3. if height[l] <= height[right] move the left pointer to the right, otherwise we move the right pointer to the left.
        we move the pointer with the shorter height inward because the max arae is limited by the shorter side. 
        edge cases: empty list, no"""

        if len(heights) == 0:
            return 0
        
        #two pointers left,right
        left,right=0,len(heights)-1
        res = 0
        #we loop until the two pointers meet
        while left <= right:
            #compute the current area
            cur_area = min(heights[left],heights[right]) * (right-left)
            res = max(res,cur_area)
            #move smaller height pointer inward
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -=1
        
        return res
