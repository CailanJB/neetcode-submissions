class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        size = 2 * len(nums)
        n = len(nums)
        ans = [0] * size
        """we know the size of the array should be 2n, so we initlize an array of that length. then go through each element in the array and add its correpsoding value to the correct index"""
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

        