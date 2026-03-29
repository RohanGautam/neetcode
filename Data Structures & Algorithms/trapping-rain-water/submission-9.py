class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxl,maxr=height[l],height[r]
        total=0

        while l<r:
            if maxl<=maxr:
                # max right can only be higher
                # the minimum is thus maxl by default at l's position
                l+=1
                if l<len(height):
                    total += max(0, maxl-height[l])
                maxl=max(maxl,height[l])
            else:
                r-=1
                if r>=0:
                    total += max(0, maxr-height[r])
                maxr=max(maxr,height[r])

        return total