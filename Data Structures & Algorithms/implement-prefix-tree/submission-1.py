
from typing import Dict

class Node:
    def __init__(self,char=None):
        self.char=char
        # self.children : list[Node] = []
        self.children : Dict[str, Node] = {}
        self.ends_here = False

class PrefixTree:
    # idea: characters as a graph

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for i,c in enumerate(word):
            if c not in cur_node.children:
                cur_node.children[c]=Node(c)

            cur_node=cur_node.children[c] # move down
            if i==len(word)-1:
                cur_node.ends_here=True

            
    def search(self, word: str) -> bool:
        cur_node = self.root
        for i,c in enumerate(word):
            if c not in cur_node.children:
                return False

            cur_node=cur_node.children[c] # move down
            if i==len(word)-1 and cur_node.ends_here==True:
                return True
        return False
                

    def startsWith(self, word: str) -> bool:
        cur_node = self.root
        for i,c in enumerate(word):
            if c not in cur_node.children:
                return False

            cur_node=cur_node.children[c] # move down
            if i==len(word)-1:
                return True
        return False
        