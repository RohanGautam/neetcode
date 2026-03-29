class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force: depends on left and right max heights
        total=0
        s = 0
        for i in range(len(height)):
            L,R = max(height[:i]+[s]), max(height[i+1:]+[s])
            water_col_vol= max(0, min(L,R)-height[i])
            # print(i, water_col_vol)
            total+=water_col_vol
        return total
        