class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # # does not work because of zeros.
        # total_prod = 1
        # for n in nums:
        #     total_prod*=n
        # return [total_prod//n for n in nums]

        # actually the challenge is only in dealing with zeros.
        # if we had a list indcating if there were zeros at any other location that would be nice.
        # prefix-suffix (after hint 3)
        p,s = [1],[1]
        for i in range(len(nums)-1):
            p_idx, s_idx = i, -(i+1)
            p.append(p[-1]*nums[p_idx])
            s.append(s[-1]*nums[s_idx])
        
        out = []
        for i in range(len(nums)):
            out.append(p[i]*s[-(i+1)])
        
        return out




        
        