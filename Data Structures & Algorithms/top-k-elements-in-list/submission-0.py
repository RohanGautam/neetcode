class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d={}
        # for n in nums:
        #     if n not in d:
        #         d[n]=0
        #     d[n]+=1
        
        # O(nlogn) because of the sort
        # return [x[0] for x in sorted(d.items(), reverse=True, key=lambda x:x[-1])][:k]

       # using a dict is an issue because it will inherently be unordered.
        d={}
        for n in nums:
            if n not in d:
                d[n]=0
            d[n]+=1
        # the count->value map should be ordered. its max len will be n
        counts = [[] for _ in range(len(nums)+1)]
        for key in d:
            counts[d[key]].append(key)
        total=k
        ans=[]
        for i in range(len(counts)-1,-1,-1):
            for item in counts[i]:
                if total==0:
                    break
                ans.append(item)
                total-=1
        return ans

