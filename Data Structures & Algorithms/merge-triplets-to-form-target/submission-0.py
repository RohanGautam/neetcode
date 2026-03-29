class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # filter invalid triplers
        triplets = [t for t in triplets if all([t[i]<=target[i] for i in range(3)])]
        # SINCE WE FILTERED invalid
        # we only need to check existence.
        # why? in maxing elements, we're not combining them, jsut choosing one over the other
        # so the actual target value has to exist
        # say we found the target at position x, but the constructed triplet has a bigger value for y than what we need - 
        # key =>this wont be the case because those possibliteis will be removed 
        res = [False]*3
        for t in triplets:
            for i in range(3):
                if t[i]==target[i]:
                    res[i]=True
        return all(res)