# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from typing import ListNode
from typing import List
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True           
        return False                    














        # curr=head
        # s=set()
        # while curr is not None:
        #     if curr not in s:
        #         s.add(curr)
        #         curr=curr.next
        #         continue
        #     if curr in s:
        #         return True    
        # return False        
        


