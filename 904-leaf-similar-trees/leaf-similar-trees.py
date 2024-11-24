# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(root, ans):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                ans.append(root.val)
            leaf(root.left,ans)
            leaf(root.right,ans)
            return ans
        ans1=leaf(root1,[])
        ans2=leaf(root2,[])
        return ans1==ans2
