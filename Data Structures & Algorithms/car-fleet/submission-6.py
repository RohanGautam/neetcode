class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort by position so we can iterate sequentially
        data = sorted(zip(position,speed), key=lambda x: x[0])
        # convert to time taken to reach destination
        times = [((target-p)/s)for p,s in data]
        c = 0
        cur=None
        for t in times[::-1]:
            if cur is None:
                cur=t
                c+=1
            else:
                if t<=cur:
                    # becomes part of my fleet
                    pass
                else:
                    cur=t
                    c+=1
        return c

         