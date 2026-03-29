class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        # computation
        # should leave out unchanged if no profitable transaction

        # want to buy low, sell high
        # no profit if no matter when you buy, the future value is cheaper
        # basically, if you buy on a day befter which the price never crosses your buying price
        
        # conversely, we will make a transaction only if there is a day after that point where the price is higher.

        # O(n^2)
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                out = max(out, prices[j]-prices[i])
        return out
        