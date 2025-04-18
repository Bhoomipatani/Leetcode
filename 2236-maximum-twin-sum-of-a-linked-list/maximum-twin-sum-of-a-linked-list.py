# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        st = []
        maximumSum = 0

        while current:
            st.append(current.val)
            current = current.next

        current = head
        size = len(st)
        count = 1
        maximumSum = 0
        while count <= size/2:
            maximumSum = max(maximumSum, current.val + st.pop())
            current = current.next
            count = count + 1

        return maximumSum