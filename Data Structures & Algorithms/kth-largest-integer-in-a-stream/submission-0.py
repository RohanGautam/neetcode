import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify(nums)
        self.h=nums
        # if only k elements in nums, then 
        while len(self.h)>self.k:
            heapq.heappop(self.h)


    def add(self, val: int) -> int:
        # add AND return the kth largest number
        heapq.heappush(self.h,val)
        while len(self.h)>self.k:
            heapq.heappop(self.h)
        return self.h[0]
