import heapq
import collections
from queue import Queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_freq_heap = [(v,k) for k,v in collections.Counter(tasks).items()]
        heapq.heapify_max(max_freq_heap)
        c=0
        q = []
        # have have empy heap but not queue, hence
        while max_freq_heap or q:
            c+=1 # time increases regardless

            if max_freq_heap:
                ele = heapq.heappop_max(max_freq_heap)
                print(ele)
                if (ele[0]-1)>0:
                    q.append(((ele[0]-1, ele[1]), c+n))
            else:
                print('idle')

            if q and q[0][-1]==c:
                # process it next
                ele = q.pop(0)[0]
                heapq.heappush_max(max_freq_heap, ele)
        return c


            

