# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
        q=[]
        ans=[]
        q.append(root)
        level=0
        prevnode=-inf
        while len(q)!=0:
            levelsize=len(q)
            
            # level=[]
            for i in range(levelsize):
                node=q.pop(0)
                nodeval=node.val
                # print(node.val, prevnode)
                if level%2==0:
                    if ((nodeval)%2==0 or prevnode>=nodeval):
                        return False
                else:
                    if (nodeval%2!=0 or prevnode<=nodeval) :
                        return False
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                prevnode=nodeval
            if level%2==0:
                prevnode=inf
            else:
                prevnode=-inf
            # print(level)
            level+=1
            # ans.append(level)
        # print(ans)
        return True
