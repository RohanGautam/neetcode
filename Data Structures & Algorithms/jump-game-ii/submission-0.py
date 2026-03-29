class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=r=0
        while r<len(nums)-1:
            newl, newr = l, r
            for i in range(l,r+1):
                newl=i+1
                newr = max(newr, i+nums[i])
            l,r = newl,newr
            res+=1
        return res


'''
The number at index i represents the maximum jump you can make from that position. But you can make smaller jumps if needed.
The goal is : return the minimum _number_ of jumps
- st_1 : jump as much as you can in each step
    -> does not because you might jump over a number that can get you to the end faster.
    -> [5, 5, 100, 1,1,......]
    -> [3, 0, 100, 1,1,......]
There is always a valid path
'''
