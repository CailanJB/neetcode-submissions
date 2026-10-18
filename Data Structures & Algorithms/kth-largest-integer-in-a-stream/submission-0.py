import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we use a min_heap and pop k times to get the k largest ele,ets. min heaps laways gurantee the smallest value is on top so removing values until theres only k values would gurmatee the k largets values since as we pop elements the bigger elemnts woul d be the rot of the heap/.
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
            
        

    def add(self, val: int) -> int:
        #now when adding elments we need to rework the heap to ensure the kth largets is at the top. we add the leemnt to the heap and if the sze of the heap goes over k we pop from the heap until there ar ek valeus
        heapq.heappush(self.minheap,val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
