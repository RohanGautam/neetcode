class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        co_map={')':'(', ']':'[', '}':'{'}
        for b in s:
            if b in co_map.values():
                l.append(b)
            if b in co_map.keys():
                if len(l)==0 or (l.pop()!=co_map[b]):
                    return False
        return True if len(l)==0 else False
        