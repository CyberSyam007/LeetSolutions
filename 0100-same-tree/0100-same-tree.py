# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(tree):
            if not tree:
                return ['#']
            return [str(tree.val)] + traverse(tree.left)+traverse(tree.right)
        x1=','.join(traverse(p))
        x2=','.join(traverse(q))
        return x1==x2
            



        
        