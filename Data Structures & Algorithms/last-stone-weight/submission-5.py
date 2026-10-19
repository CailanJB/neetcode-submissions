import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Brute force we can sort the array and continously query the firts two indices in a stack and do the operations.,
        O(n log n) complexity due to sorting
        insead we can use a amx heap therefore the largets value is always at the top. we pop two elements from the top until the heap only contain1 item."""
        if len(stones) == 0:
            return -1
        
        if len(stones) == 1:
            return stones[0]
        
        #first negate eveyr value in stones to make max heap. the biggest value would be the most negative value which is the the smllest value so the heap would build corretcly/.
        #after the algorithm runs if the heap becomes empty we just return 0. the heap can be empty if we have an even number of values and eveyr value is strictly less than the next ele,ent.
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_value = heapq.heappop(stones)
            second_value = heapq.heappop(stones)
            if first_value < second_value:
                y = -(second_value - first_value)
                heapq.heappush(stones,y)
        
        stones.append(0)
        return abs(stones[0])

        