import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # just the reverse right, the min heap?
        h = []
        for n in nums:
            if len(h)==k :
                if n>h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h,n)
            else:
                heapq.heappush(h,n)
        return h[0]
