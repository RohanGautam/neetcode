class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # @review 1 : look on both sides starting from each bar
        max_area=0
        for i in range(len(heights)):
            # look both ways
            l,r = i,i
            while (l-1)>=0 and heights[l-1]>=heights[i]:
                l-=1
            while (r+1)<len(heights) and heights[r+1]>=heights[i]:
                r+=1
            # print(heights[i],l,r)
            max_area = max(max_area, heights[i]*(r-l+1))
        return max_area
