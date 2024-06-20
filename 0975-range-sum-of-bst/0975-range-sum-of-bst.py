# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=[]
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            return res
        ans=[]
        summ=0
        ans=inorder(root)
        for num in ans:
            if num>=low and num<=high:
                summ+=num
        return summ