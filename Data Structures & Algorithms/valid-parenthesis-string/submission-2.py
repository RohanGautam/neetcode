class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        unprocessed = 0
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False                  
            else:
                stars.append(i)
        # need to handle the ( now
        for idx in stack[::-1]:
            if stars:
                star_id = stars.pop()
                if star_id<idx:
                    return False
            else:
                return False
        return True



# main part -> how to take * into account -> just a stack operation otherwise.
# Every time you encounter a branch , try both ( and ) in place of * and see if it leads to a valid parenthesis string
#      -> can quickly have exponential number of possibilities (2^n)
# example : "((**)"
# st_1: add `(` to a stack, and pop it off when you encounter either a `)` OR a `*`
#    (example) - s=[((] -> * -> s=[(] -> * -> s=[] -> ) -> nothing to pop
#    - not clear how to actually check if things were valid at the end
# st_2: do a normal parenthesis check with a stack and add up remaining `(` or `)`. if this is more than the number of *s, then it's not valid.
#    (example) s=[((] -> ** (ignore) -> ) -> s=[(] -> two *s remaining -> valid (len(s)+remaining `)`) <= *s
#    - is lesser than equal not equal because *s can also be empty
#    - * is a physical placeholder. `*(` with this logic is currently true, but should be false, because the order of where * is matters, which this strategy ignores
# st_3 : in the loop when we reach ) and the stack is empty, we account for the starts available at the current step, instead of accounting for them at the end. alsom dont account for remaining (, jsut remaining )
#    - example `*()(` -> want this to be false
#    - * -> sc=1 -> ( -> s[(] -> ) -> s=[] -> ( -> s=[(] -> unacc =0<=1
# st_4 : keep track of indices in the stacks since we have to see stars for those as well.
#    - st_3 handles the stars for )
#    - basically ensure that valid stars are the ones that are to the RIGHT of the unmatched (











