# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans=[]
        q=[]
        if root is None:
            return 0
        q.append(root)
        while len(q)!=0:
            levelsize=len(q)
            level=[]
            for i in range(levelsize):
                node=q.pop(0)
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            print(level)
            ans.append(sum(level))
            print(ans)
        minv=ans[0]
        minl=0
        for i in range(1,len(ans)):
            if ans[i]>minv:
                minv=ans[i]
                minl=i
            
        return minl+1
                