class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """1st approach we can sort the entire array and check the ,ongest sequence since thre in order. For each index we keep track of its streak by checking if that number + 1 is inside the array. we do this for every number. if num + 1 is inside the array we incrment the count and icnrement num to see if the next value is also inside the array.
        This would take us 0(n^2) time to complete due to the expensive check of checking if num + 1 is in the array.
        
        optmal apprach: We can put nums in a set so the check for num+1 takes consant time instead"""
        
        #brut force for each number we can check in num + 1 is in the array and keep track untl the streak is broken/
        if len(nums) == 0:
            return 0
        seen = set(nums)
        best_streak = 1
        

        for num in nums:
            curr_streak = 1
            if num - 1 not in seen:
                cur_num = num
                #this is the start of a streak
                while cur_num + 1 in seen:
                    curr_streak+=1
                    cur_num+=1

            best_streak = max(curr_streak,best_streak)
        
        return best_streak
    