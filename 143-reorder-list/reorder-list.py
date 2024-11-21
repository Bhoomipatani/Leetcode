# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr=[]
        curr=head
        carr=[]
        while head:
            arr.append(head.val)
            head=head.next
        n=len(arr)
        for i in range((n//2 )+1):
            carr.append(arr[i])
            carr.append(arr[n-i-1])
        i=0
        while curr:
            curr.val=carr[i]
            curr=curr.next
            i+=1
        return head