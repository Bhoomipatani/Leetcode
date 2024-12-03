# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def inorder(root):
            nonlocal ans
            if root is None:
                return True
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            return ans
        inorder(root)
        for i in range(1,len(ans)):
            if ans[i-1]>=ans[i]:
                return False
        return True