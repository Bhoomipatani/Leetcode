# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes=0
        def dfs(root,maxsofar):
            nonlocal num_good_nodes
            if root is None:
                return
            if maxsofar<=root.val:
                num_good_nodes+=1
            dfs(root.left, max(maxsofar,root.val))
            dfs(root.right, max(maxsofar,root.val))
        dfs(root, -inf)
        return num_good_nodes