class Solution:
    '''15 feb review'''
    def trap(self, height: List[int]) -> int:
        # the main idea is that the water column at a given index
        # is the min of the maximums on either side minus it's height
        # the natural solution(to me) uses prefix arrays
        # that track maxes from either direction
        maxleft,maxright=[],[]
        for i in range(len(height)):
            j = len(height)-i-1

            if len(maxleft)==0:
                maxleft.append(height[i])
            else:
                maxleft.append(max(height[i],maxleft[-1]))
            if len(maxright)==0:
                maxright.append(height[j])
            else:
                maxright.append(max(height[j],maxright[-1]))
        
        maxright=maxright[::-1]
        area=0
        # print(maxleft, maxright)
        for i in range(len(height)):
            a=max(0, min(maxleft[i],maxright[i])-height[i])
            # print(i, maxleft[i],maxright[i],a)
            area+=a
        return area
            
            
