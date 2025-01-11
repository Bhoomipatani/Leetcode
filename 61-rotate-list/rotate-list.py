# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr=head
        if k<=0 or head is None:
            return head
        l=1
        while curr.next is not None:
            curr=curr.next
            l+=1
        k=k%l
        if k==l or l<=1 or k==0 :
            return head

        start=head
       
        curr.next=start
        curr=curr.next
        i=l-k
        while i!=1:
            curr=curr.next
            i-=1
        head1=curr.next
        curr.next=None
        return head1

