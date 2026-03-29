class Node:
    def __init__(self,char=None):
        self.char=char
        self.children : list[Node] = []
        self.ends_here = False

class PrefixTree:
    # idea: characters as a graph

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for i,c in enumerate(word):
            found = False
            for n in cur_node.children:
                if n.char==c:
                    cur_node=n
                    found=True
                    break
            if found: 
                if i==len(word)-1:
                    cur_node.ends_here=True
                continue
            else:
                n = Node(c)
                if i==len(word)-1:
                    n.ends_here=True
                cur_node.children.append(n)
                cur_node=n

            
    def search(self, word: str) -> bool:
        # this is for the whole word.
        cur_node = self.root
        for i,c in enumerate(word):
            found = False
            for n in cur_node.children:
                if n.char==c:
                    cur_node=n
                    found=True
                    break
            if found: 
                if i==len(word)-1 and cur_node.ends_here:
                    return True
                continue
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for i,c in enumerate(prefix):
            found = False
            for n in cur_node.children:
                if n.char==c:
                    cur_node=n
                    found=True
                    break
            if found: 
                # but not necessarily ending here
                if i==len(prefix)-1:
                    return True
                continue
            else:
                return False
        return False
        
        