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
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         out = max(out, prices[j]-prices[i])

        # sorting based
        # s_idx = sorted(range(len(prices)),key=lambda x : prices[x])
        # print(s_idx)
        # for i in range(len(prices)-1):
        #     # still O(n^2) actually, because you cant just check pairwise
        #     # doing so will lead to a lot of missed candidates
        #     a,b = s_idx[i], s_idx[i+1]
        #     if a<b and prices[a]<prices[b]:
        #         out = prices[b]-prices[a]
        
        # b,s = 0,1
        # p = 0
        # for i in range(len(prices)):
        #     # i is where you sell
        #     if i>b and (prices[i]-prices[b])>p:
        #         s=i
        #         p=prices[i]-prices[b]
        #     # if i is where you buy
        #     if i<s and (prices[s]-prices[i])>p:
        #         b=i
        #         p=prices[s]-prices[i]

        # after hint 3
        b = 0
        p=0
        for i in range(len(prices)):
            if prices[i]-prices[b]>p:
                p = prices[i]-prices[b]
            if prices[i]<prices[b]:
                b=i
            
        return p
        