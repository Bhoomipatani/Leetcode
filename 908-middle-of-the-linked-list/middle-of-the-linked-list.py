# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next
        mid=(count//2)+1
        temp = head

        while temp is not None:
            mid = mid -1
            if mid == 0:
                break
            
            temp = temp.next
        return temp