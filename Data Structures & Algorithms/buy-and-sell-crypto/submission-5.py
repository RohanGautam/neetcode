class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice=100 # max acc to problem
        for p in prices:
            # track the min price
            if p<minprice:
                minprice=p
            if p-minprice>profit:
                profit = p-minprice
        return profit
            
        