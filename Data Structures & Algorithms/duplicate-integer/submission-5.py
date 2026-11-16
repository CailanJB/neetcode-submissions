class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Brute force: use double loop checking for every value if a duplicate exist
        optimal: use a set to keep track of elemnts we saw"""
        if len(nums)==0:
            return False
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        