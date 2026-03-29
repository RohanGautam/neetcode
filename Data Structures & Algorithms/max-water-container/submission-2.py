class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        res=0
        while i<j:
            area = (j-i)*min(heights[i],heights[j])
            if area>res:
                res=area
            # key idea: move only the shorter wall.
            # moving the bigger one will only make the area stay 
            # the same or decrease.
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return res