class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=sorted(nums)
        out=set()
        for i in range(len(l)-2):
            j,k=i+1,len(l)-1
            target=-l[i]
            while j<k:
                val = l[j]+l[k]
                if val>target:
                    k-=1
                elif val<target:
                    j+=1
                else:
                    out.add((l[i],l[j],l[k]))
                    j+=1
        return list(out)