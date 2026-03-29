import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones)>1:
            # heap because repeated max extractions
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x!=y:
                heapq.heappush_max(stones, (x-y))
        return stones[0] if stones else 0