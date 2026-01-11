class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class Doubly_linked_list:
    def __init__(self):
        self.head=None

    def Insert_at_head(self,val):
        new_Node=Node(val)
        if not self.head:
            self.head=new_Node
        else:
            new_Node.next=self.head
            self.head.prev=new_Node
            self.head=new_Node

    def append(self,value):
        new_Node=Node(value)
        if not self.head:
            self.head=new_Node
            
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_Node
            new_Node.prev=curr

    def print_link_list(self):
        if not self.head:
            return None
        else:
            curr=self.head
            while curr is not None:
                print(curr.val, end="")
                if curr.next!=None:
                    print("<->",end='')
                curr=curr.next    

    def count_length(self):
        count=0
        print()
        if not self.head:
            return 0
        else:
            curr=self.head
            while curr:
                count+=1
                curr=curr.next
        return count                    

    def insert_in_between(self, val, index):
        new_node = Node(val)

        # Case 1: empty list
        if not self.head:
            if index == 0:
                self.head = new_node
                return
            else:
                print("Index out of range")
                return

        # Case 2: insert at head
        if index == 0: 
            self.Insert_at_head(val)
            return

        # Traverse to index-1
        curr = self.head
        count = 1

        while curr and count < index - 1:
            curr = curr.next
            count += 1

        if not curr:
            print("Index out of range")
            return

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node

        curr.next = new_node

    def delete_from_end(self):
        if not self.head:
            return None
        elif self.head.next is None:
            self.head=None
            return
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.prev.next=None
            



dl=Doubly_linked_list()
dl.append(10)
dl.append(20)
dl.append(30)
dl.append(40)
dl.append(50)
dl.append(60)
dl.append(70)
dl.append(80)
dl.append(90)
dl.print_link_list()            
print(dl.count_length())
dl.insert_in_between(50,2)
dl.print_link_list()   
dl.delete_from_end()
print()
dl.print_link_list()
     

