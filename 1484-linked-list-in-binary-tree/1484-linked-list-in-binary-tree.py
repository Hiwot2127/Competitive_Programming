# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(tree_node, list_node):
            if list_node is None:  
                return True
            if tree_node is None: 
                return False
            if tree_node.val != list_node.val:
                return False
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
        if not root:
            return False
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)