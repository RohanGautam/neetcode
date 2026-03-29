class Solution:
    def trap(self, height: List[int]) -> int:
        # we can precompute the maximums from the left and the right
        # "prefix arrays" - use for "max seen so far for this" logic
        
        maxleft, maxright=[],[]
        for i in range(len(height)):
            if i==0:
                maxleft.append(height[i])
            else:
                maxleft.append(max(height[i],maxleft[-1]))
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                maxright.append(height[i])
            else:
                maxright.append(max(height[i],maxright[-1]))
        
        maxright = maxright[::-1]
        total=0
        s = 0
        for i in range(len(height)):
            L,R = maxleft[i],maxright[i]
            water_col_vol= max(0, min(L,R)-height[i])
            # print(i, water_col_vol)
            total+=water_col_vol
        return total