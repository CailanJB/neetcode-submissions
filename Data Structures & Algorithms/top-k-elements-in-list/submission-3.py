class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """1. Approach we can get the count of each element via a hashmap and sort the hashmap by values and return the top k.'
        darwback: this takes O(n log n) time
        Approach 2. We can use bucketsort we can make an array of size len(arr) where each index represents the count. for exaple index 1 would contain all elements in the array with a count of 1 etc.
        3. to get the top k most frequnet elemnts we sart from th eback of the array and stop until we reach k
        0(n) time
        O(n) space
    3. We can also use a min-heap. We add each element to the heap and once we go over k we pop from the heap and by the tiem the heap is empty the top k most frequnet elemns would appear in the heap"""
        
        if len(nums) == 0:
            return []

        #we use plus 1 because the count for an elemnt can be exactly len(nums) so we need an inde for that
        bucket_arr = [[] for _ in range(len(nums)+1)]
        res = []

        freq_count = Counter(nums)
        
        #insert the counts of each element at their appropiate slot
        for key,val in freq_count.items():
            bucket_arr[val].append(key)
        
        #work from back of the array and add the elets until we reah size k
        for i in range(len(bucket_arr)-1,0,-1):
            if len(bucket_arr[i]) != 0:
                for num in bucket_arr[i]:
                    if len(res)==k:
                        break
                    res.append(num)
                    
            
       
        return res

        
        
