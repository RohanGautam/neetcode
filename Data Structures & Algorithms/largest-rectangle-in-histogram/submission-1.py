class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force attempt
        # idea: go through each min and expand as much as you can in neighbourhood
        mins_to_check = sorted(list(set(heights)))
        max_area=0
        for m in mins_to_check:
            # for each instance of the min value, spread in both directions
            for i in range(len(heights)):
                if heights[i]==m:
                    l,u=i,i
                    # search right:
                    while l>=0 and heights[l]>=m:
                        l-=1
                    else:
                        # runs when condition no longer true
                        # damn ugly
                        l+=1
                    # search left
                    while u<len(heights) and heights[u]>=m:
                        u+=1
                    else:
                        l+=1

                    width = (u-l)+1
                    height=m
                    area = width*height
                    if area>max_area:
                        max_area=area
                        print(area,m,i,l,u)
        return max_area
