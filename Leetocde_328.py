# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import ListNode
from typing import List

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd=head
        even=odd.next
        even_head=even

        while even and even.next:
            odd.next=even.next
            odd=odd.next

            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head    