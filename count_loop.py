

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
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
    
s=Solution()
s.detectCycleaa    