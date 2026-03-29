class Solution:
    def area(self, heights,i,j):
        return min(heights[j],heights[i])*abs(j-i)
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        v = self.area(heights,i,j)
        while i<=j:
            a = self.area(heights,i,j)
            if a>=v:
                v=a
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
            # a1 = self.area(heights,i+1,j)
            # a2 = self.area(heights,i,j-1)
            # if a1>v:
            #     v=a1
            #     i+=1
            # elif a2>v:
            #     v=a2
            #     j-=1
            # else:
            #     i+=1
            #     j-=1
        return v



        