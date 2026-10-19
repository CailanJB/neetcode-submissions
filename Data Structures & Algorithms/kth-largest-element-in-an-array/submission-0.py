import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """We use a min heap. we add each element to the min heap and when the size is over k we extarct. this way the k largets eleemtns remian."""
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        largest_k = 0
        return heap[0]
            
        
        