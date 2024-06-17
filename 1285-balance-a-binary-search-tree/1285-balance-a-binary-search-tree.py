# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)

        a=inorder(root)
        def build(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(a[mid])
            root.left=build(left,mid-1)
            root.right=build(mid+1,right)
            return root
        return build(0,len(a)-1)