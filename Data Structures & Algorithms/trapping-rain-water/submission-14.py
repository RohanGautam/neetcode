class Solution:
    def trap(self, height: List[int]) -> int:
        # need max heights from both sides.
        l,r = [],[]
        for i in range(len(height)):
            e1,e2 = height[i], height[len(height)-1-i]
            if i==0:
                l.append(e1)
                r.append(e2)
            else:
                l.append(max(e1,l[-1]))
                r.append(max(e2,r[-1]))
        w = 0
        r=r[::-1]
        # print(r)
        for i in range(len(height)):
            vol = max(0,min(l[i],r[i])-height[i])
            # print(height[i],vol, l[i],r[i])
            w+=vol
        return w