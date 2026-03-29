class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return min(cost)
        else:
            # base case
            cache = {0:cost[0],1:cost[1]}        
            def mc(index):
                print(index,cache)
                # base cases + cache check
                if index in cache:
                    return cache[index]
                # recursive step
                c = min(mc(index-1),mc(index-2))
                if index<len(cost):
                    c+=cost[index]
                cache[index]=c
                return cache[index]
    
            return mc(len(cost))

# [1,2,3]
# mc(3)
# c->min(mc(2),mc(1)) -> 2
    # mc(1)->2
    # mc(2) -> min(mc(1),mc(0)) + 3 -> min(2,1)+3 -> 4

# [1,2,1,2,1,1,1]
# mc(7)
# c->min(mc(6),mc(5))
    # mc(5) = min(mc(4),mc(3))+1
