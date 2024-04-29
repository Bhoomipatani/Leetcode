# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=curr=head
        count=0
        while curr is not None:
            curr=curr.next
            count+=1
        num=count-n
        print(num)
        if num==0:
            head=head.next
        while num>1:
            temp = temp.next
            num -= 1
            if num == 0:
                break
            
        print(temp)
        if temp.next is not None:
            temp.next=temp.next.next
      
        return head
