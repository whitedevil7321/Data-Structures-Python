
from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left =None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
        self.queue=deque()
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            self.queue.append(self.root)
            return
        else:
            
            qq=self.queue.copy()
            while qq:
                item=qq.popleft()
                if not item.left:
                    item.left=new_node
                    self.queue.append(new_node)
                    break
                else:
                    item.right=new_node
                    self.queue.append(new_node)
                    break






    
