from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """1, Naive approach: Is get the count for each number via a hashmap or Counter
        Sort the map from greatest to least and loop through the k results. O(n log n) due to sorting
        list.sort(lambda x: x[0], reverse=True)
        2. Approach : use a max-heap storing the counts.Then pop k times from the max heap. O(k log n) rutnime
        3. Optimal solution: Bucket sort. The indices of the buckets will be the counts. and we place the counts of the numbers in their respective bukcet. Then start from the back of the arrau and add to the result array until it excedes k or we reach the end of the list. O(n) time, O(N) space"""

        #edge case: empty array
        if len(nums) == 0:
            return []
        
        #get the count of each number
        counts = Counter(nums)
        #create buckets array. index i represnets a count, +1 to account for last index being len(nums)
        #with list comprehension each array has its own spot in memory
        #with list multiplication [[]] * len(nums) + 1, each copies its reference so updating one block updates all of them. 
        bucket_arr = [[] for i in range(len(nums) + 1)]
        #loop through each number in counts
        for num,count in counts.items():
            bucket_arr[count].append(num)
       
        
        #loop starting from the back of bucket_arr
        result = []
        for i in range(len(bucket_arr)-1,0,-1):
            #if not empty add the elemnt to result
            if len(result) == k:
                break
            if len(bucket_arr[i]) != 0:

                #add all elements to the result
                for val in bucket_arr[i]:
                    result.append(val)
                

        return result

