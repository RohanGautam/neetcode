class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in range(len(numbers)-1):
        #     lower, upper = i, len(numbers)-1

        #     # binary search for the corresponding sum (else continue)
        #     # we can use it since the array is sorted.
        #     while lower<=upper:
        #         middle = lower+(upper-lower)//2
        #         val=numbers[i]+numbers[middle]
        #         if val>target:
        #             upper=middle-1
        #         elif val<target:
        #             lower=middle+1
        #         else:
        #             return [i+1,middle+1]
        # return None

        i,j=0,len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1,j+1]
        return None
            


