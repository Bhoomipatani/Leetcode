# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def rightview(root,level,arr):
            if not root:
                return
            if level==len(arr):
                arr.append(root.val)
            rightview(root.right, level+1, arr)
            rightview(root.left, level+1, arr)
            return arr
        return rightview(root,0,[])