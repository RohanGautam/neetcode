class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        co_map={')':'(', ']':'[', '}':'{'}
        for b in s:
            if b in co_map.values():
                stack.append(b)
            else:
                if len(stack)>0:
                    if stack.pop()!=co_map[b]:
                        return False
                else:
                    return False
        if len(stack)>0:
            return False
        return True
