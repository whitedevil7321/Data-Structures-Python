
from typing import Optional
from typing import ListNode
from typing import List
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node        

    def PrintLinkedList(self):
        if self.head is None:
            print("Empty Linked List")
            return

        curr = self.head
        while curr is not None:
            print(curr.val, end="")
            if curr.next is not None:
                print(" -> ", end="")
            curr = curr.next
        print()  


    # # def PrintLinkedList(self):
    #     if self.head is None:
    #         print("Empty Linked List")
    #         return

    #     curr = self.head
    #     while curr is not None:
    #         print(curr.val, end="")
    #         if curr.next is not None:
    #             print(" -> ", end="")
    #         curr = curr.next
    #     print()
                    

    def insert_after(self,target,val):
        if self.head==None:
            print('There is Nothing in the Linked List')
        else:    
            curr=self.head
            while curr.next!=None:
                if curr.val==target:
                    new_Node=Node(val)
                    
                    new_Node.next=curr.next
                    curr.next=new_Node
                    break
                curr=curr.next    

    def Insert_At_Specific_Index(self,index,val):
        if self.head==None:
            print("Lineked List Is Empty")
        elif index==0:
            new_Node=Node(val)
            new_Node.next=self.head
            self.head=new_Node
        else:
            counter=0
            curr=self.head
            while curr.next!=None:
                if counter==index-1:
                    new_Node=Node(val)
                    new_Node.next=curr.next

                    curr.next=new_Node
                    break
                counter+=1
                curr=curr.next

    def delete_element_at_index(self,index):
        if self.head==None:
            print("Link List is Empty")
        elif index==0:
            self.head=self.head.next
        else:
            counter=0
            curr=self.head
            while curr.next!=None:
                if counter==index-1:
                    curr.next=curr.next.next
                counter+=1    
                curr=curr.next        


    def reverse(self):
        if self.head==None:
            print("Linked List is Empty")
            return
            
        prev=None
        temp=self.head
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev        

    def detectCycle(self, head: Optional[Node]) -> Optional[Node]: # type: ignore
        slow=head
        fast=head
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                count=1
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                slow=slow.next    
                while slow!=fast:
                    slow=slow.next
                    count+=1    
                return count   
        return 0      



        
                    



                

    

ll=SinglyLinkedList()
ll.append(10)
ll.append(10)
ll.append(10)
ll.append(10)
ll.append(10)
ll.append(5)
ll.append(10)
ll.append(10)

ll.append(10)
ll.insert_after(5,12)
ll.insert_after(12,13)
ll.insert_after(13,14)

ll.Insert_At_Specific_Index(3,100)
ll.Insert_At_Specific_Index(0,100)

ll.PrintLinkedList()
# ll.delete_element_at_index(7)



ll.PrintLinkedList()

ll.reverse()
ll.PrintLinkedList()
ll.detectCycle(ll.head)
