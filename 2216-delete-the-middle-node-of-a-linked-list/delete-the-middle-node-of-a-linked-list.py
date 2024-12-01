# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow=fast=prev=head
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        # print(slow.val)
        if prev.next and prev.next.next:
            prev.next=prev.next.next
        else:
            prev.next=None
        return head