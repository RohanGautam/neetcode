import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # brute force -> O(n) compute vector magnitude
        # O(n logn) with sort
        # O(n) build heap + O(klogn) extract couple of times 
        dists = [((p[0]**2+p[1]**2), p)for p in points]
        res = []
        for d in dists:
            if len(res)<k:
                heapq.heappush_max(res,d)
            else:
                # the result is stored in the max heap
                # if current element is bigger than max in the k-len heap, jus tignore it
                # otherwise add it - uses lesser space, you dont have to heapify the whole thing
                if d<res[0]:
                    heapq.heappop_max(res)
                    heapq.heappush_max(res,d)
        return [r[-1] for r in res]