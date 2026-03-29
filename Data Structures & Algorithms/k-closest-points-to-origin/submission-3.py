import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # brute force -> O(n) compute vector magnitude
        # O(n logn) with sort
        # O(n) build heap + O(klogn) extract couple of times 
        dists = [((p[0]**2+p[1]**2)**0.5, p)for p in points]
        heapq.heapify(dists)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(dists)[-1])
        return res