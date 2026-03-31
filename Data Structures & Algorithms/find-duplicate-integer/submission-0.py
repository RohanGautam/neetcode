class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        v,f=nums[0],1
        for n in nums[1:]:
            print(v,f)
            if n==v:
                f+=1
            elif f==1:
                v,f=n,1

            if f>1:
                return v

'''
st_1 : trivial would be to just ave a hashmap of counts and take the maximum, but the hashmap will take O(N) extra space.
Challenge:
- not modifying input array (ex: sorting would make this work)
- no extra space
- basically, just iterating through the aray costant 
  number of times and possible some constant memory (which will be O(1))

maybe jsut the current most freq and its value
st_2: store val,freq. each incoming element overwrites this with freq 1 (unless current val is 0), unless it's been seen before in which case the freq is appended
- [1,1,2,2,2,3] -> not possible by the problem statement - if it was, strategy wouldnt work
- [1,1,2,3,4] (1,1 as val:freq) -> (1,2) since freq more than one -> return 1
- [1,2,3,3,4] (1,1)->(2,1)->(3,1)->(3,2)->3
- [1,2,3,4,4] ... (4,2) ->4
- [1,2,1,3,4] (1,1)->(2,1)->(1,1)->3,1->4,1 -> info lost
- => this strategy would only work if the input array is sorted to allow for frequencies to stack
- still O(1) extra space though, so thats an improvement

the problem was tagged linked list -> how would that help?
if the ll is nodes of unique values, we can assume the input is a path on the linked list
[1,2,1,3,4]
ll: 1 -> 2 -> 3 -> 4
    ^----|
    |---------^
but what does it mean for 1->3?
'''