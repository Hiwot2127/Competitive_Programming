# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            nonlocal cur,count,maxc,mode
            if not node:
                return
            traverse(node.left)
            count= count+1 if node.val==cur else 1
            cur=node.val
            if count>maxc:
                maxc=count
                mode=[cur]
            elif count==maxc:
                mode.append(cur)
            traverse(node.right)
        cur,count,maxc,mode=None,0,0,[]
        traverse(root)
        return mode
        