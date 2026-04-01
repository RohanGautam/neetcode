class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res^=n
        return res


'''
We have a list of numbers, where every number except one occurs twice. the odd one out appears only once.
Let's think:
st1: frequency counts, but this takes O(n) _extra_ space.

use an integer to represent if number at position 1 seen before or not
this would mean since len of nums can be 10000, we would need a 10000 bytes , best we can do is 64 bit with 512 bytes
so number->position is not a good strategy.

how will we uniquely identify which number has only one?
maybe one bucket for everything seen twice, one for seen once, but storing all seen still O(N/2=N)



'''