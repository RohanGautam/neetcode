class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for sidx in range(len(gas)):

            cur = sidx
            g=0
            # next = (cur+1)%len(gas)
            while cur is not None:
                g += gas[cur]
                # for going to the next
                g = g-cost[cur]
                print(sidx, cur, g)
                if g>=0:
                    # you were able to reach
                    cur = (cur+1)%len(gas)
                    if cur == (sidx)%len(gas):
                        break
                else:
                    cur=None
            if cur==(sidx)%len(gas):
                return sidx
        return -1