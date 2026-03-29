class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position,speed), key=lambda x:x[0])
        times = [(target-arr[i][0])/arr[i][1] for i in range(len(arr))]
        c=1
        i = len(times)-1
        print(arr)
        print(times)

        blocker=None
        for i in range(len(times)-1,0,-1):
            if i==len(times)-1:
                blocker=times[i]
            if times[i-1]<=blocker:
                # joins fleet, not affecting number of fleets
                pass
            else:
                blocker=times[i-1]
                c+=1
        return c
