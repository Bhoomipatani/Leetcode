# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=[]
        if not root:
            return 0
        q.append(root)
        level=0
        while len(q)!=0:
            size=len(q)
            # print(len(q))
            for i in range(size):
                root=q.pop(0)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            level+=1
        return level