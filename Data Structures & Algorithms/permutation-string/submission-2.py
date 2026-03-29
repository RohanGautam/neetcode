class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        else:
            ds1 = {}
            for c in s1:
                ds1[c]=ds1.get(c,0)+1
            
            ds2={k:0 for k in ds1.keys()}
            for i in range(0,len(s2)-len(s1)+1):
                # # this approach does not work because you cna have the sets be the same
                # # but s1 can have repeating characters which are not accounted for in the substring
                # if len(set(s2[i:i+len(s1)]).intersection(s1_set))==len(s1_set):
                #     print(s2[i:i+len(s1)])
                #     return True
                if i==0:
                    for c in s2[i:i+len(s1)]:
                        if c in ds2:
                            ds2[c]+=1
                else:
                    prev,next = s2[i-1], s2[i+len(s1)-1]
                    if prev in ds2:
                        ds2[prev]-=1
                    if next in ds2:
                        ds2[next]+=1
                if ds1==ds2:
                    return True

            return False