from typing import Optional
from typing import ListNode
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast by 2 steps, slow by 1 step
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # slow now points to the middle node
        return slow
