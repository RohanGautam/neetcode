class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)-1):
            lower, upper = i, len(numbers)-1

            while lower<=upper:
                middle = lower+(upper-lower)//2
                val=numbers[i]+numbers[middle]
                if val>target:
                    upper=middle-1
                elif val<target:
                    lower=middle+1
                else:
                    return [i+1,middle+1]
        return None
