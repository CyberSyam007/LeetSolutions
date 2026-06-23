# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root):
            if not root:
                return '#'
            return str(root.val) + isSame(root.left) + isSame(root.right)
        
        x=isSame(subRoot)

        def Traverse(root):
            if not root:
                return
            y=isSame(root)
            if x==y:
                return True
            
            return Traverse(root.left) or Traverse(root.right)
            
        if Traverse(root)==True:
            return True
        else:
            return False
        



        