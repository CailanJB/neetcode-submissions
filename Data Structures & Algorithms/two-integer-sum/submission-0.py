class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in a):
                return [a[complement],i]
            a[nums[i]] = i
        return []    