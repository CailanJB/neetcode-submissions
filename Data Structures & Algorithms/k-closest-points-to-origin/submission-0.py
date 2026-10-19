import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Brute force: We can calcuate the euclidean distance from the orign to each point using x^2 + y^2 we dont need to use he square root because we only care about the order not the exact distance. The square tooy would just shrink the values and since we onlt care for the order no need to use it. After we sort each distance and return the points associated with the smallest distabces. O(n log n).
        Optimal approach: We can use a max_heap instead. Sfter calcualting the distances (dist,x,y) we negate the distnaces ot build a max heap. We keep popping the value from the top until the size of the max_heap no longer excedes k. 
        Why this works? When we want to find the k smallest/closest points using a max heap would move th ebiggets values to the top so after popping k times we would be left with the rmeianing values which would be the k smallest values since opping would remove the bigger values. 
        This apprach applies if we wanted to find the k largest points we would instead use a min heap and pop until the heap is of size k then the remianing values are the k largest values. 
        These approaches are more efficent and run in O(n log k)
        if we used a min_heap or max_heap for the respective problem if would instead take   O(k log n) which is more expensive because on eveyr pop we change the entire heap whereas with the optimla approach we would have k elements in the heap not all n."""

        if len(points) == 0:
            return [[]]
        
        
        #get the distances and add to array (dist,x,y): largets distance is at the top. we pop continosuly until we have k left
        distances = []
        for point in points:
            dist = -(point[0]**2 + point[1]**2)
            heapq.heappush(distances,(dist,point[0],point[1]))
            if len(distances) > k:
                heapq.heappop(distances)
        
        #now we should have the k cloest values(k smallest distances to the origin)
        result = []
        while distances:
            dist,x,y = heapq.heappop(distances)
            result.append([x,y])
        
        return result
        
       

            
            
        