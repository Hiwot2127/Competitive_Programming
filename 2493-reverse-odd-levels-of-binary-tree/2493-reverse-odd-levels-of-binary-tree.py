# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(a,b,odd):
            if a is None or b is None:
                return
            if odd:
                a.val, b.val= b.val, a.val
            rev(a.left,b.right, not odd)
            rev(a.right,b.left, not odd)
        rev(root.left,root.right,odd=True)
        return root
        
        