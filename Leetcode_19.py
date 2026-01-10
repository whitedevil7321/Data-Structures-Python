# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and n==1:
            return None
        slow=head
        fast=head
        for i in range(0,n):
            fast=fast.next
        if not fast:
            return head.next

        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next        
        return head

                    













        # curr=head
        # count=0
        # while curr:
        #     count+=1
        #     curr=curr.next

        # remaining=count-n
        # if remaining==0:
        #     head=head.next
        #     return head


        # new_head=head    
        # for i in range(remaining):
        

        #     if i==remaining-1:
        #         new_head.next=new_head.next.next



        #     new_head=new_head.next
        # return head    

