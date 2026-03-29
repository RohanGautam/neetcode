class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force attempt v2, cleaned up
        # idea: go through each element and expand as much as you can in neighbourhood
        max_area=0
        for i in range(len(heights)):
            l,u=i,i
            # search right:
            while l>=0 and heights[l]>=heights[i]:
                l-=1
            else:
                # runs when condition no longer true
                # damn ugly
                l+=1
            # search left
            while u<len(heights) and heights[u]>=heights[i]:
                u+=1
            else:
                l+=1
            # area calculation
            area = ((u-l)+1)*heights[i]
            if area>max_area:
                max_area=area
        return max_area
