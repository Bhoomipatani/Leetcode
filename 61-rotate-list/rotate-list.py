# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        curr=head
        if k<=0 or head is None:
            return head
        while curr is not None:
            curr=curr.next
            l+=1
        
        if k>l:
            k=k%l
        if k==l or l<=1 or k==0 :
            return head

        start=partition=head
        i=l-k
        while i!=1:
            partition=partition.next
            i-=1
            
        phead=partition.next
      
        partition.next=None

        head2=phead
        i=k
        while phead.next is not None:
            phead=phead.next
            i-=1
        phead.next=start

        return head2

