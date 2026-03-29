class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        cur=0
        res=0
        for i in range(1,len(prices)):
            if prices[cur]<prices[i]:
                res+=prices[i]-prices[cur]
            cur=i
            # else
        return res

'''
You can make multiple transactions. you have to sell current before buying.
- st_1 : keep track of the minimum and update the max with it as you see the elements. Each item plays the role of min and the max
    - this gives the one single most profitiable transaction
    - does not take into acocunt multiple transactions
- st_2 : the moment you see a profit, you cash in and sell. add to current profit
'''