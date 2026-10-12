class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Since the array is sorted we can just use two pinters on each side. If the sum of each pointer is bigger than target then we move the right pointer since its domnaitng the sum"""
        l,r=0,len(numbers)-1
        #stoo when the two pointers meet
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum < target:
                #move left pointer inwards
                l+=1
            else:
                r-=1
        
        return []
            

        