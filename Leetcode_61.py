# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        tail=head
        n=1
        
        while tail.next!=None:
            tail=tail.next
            n+=1
        tail.next=head
        j=1
        k=k%n
        remain=n-k
        while j!=remain:
            head=head.next
            j+=1
        current=head
        head=head.next
        current.next=None
        return head

        