# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        low=-inf
        high=inf
        def validate(root,low,high):
            if root is None:
                return True
            if root.val<=low or root.val>=high:
                return False
            return validate(root.left,low,root.val) and validate(root.right,root.val,high)
        return validate(root,low,high)