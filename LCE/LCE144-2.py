#Given the root of a binary tree, return the preorder traversal of its nodes' values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            #Since we want to traverse left subtree first in preorder
            # we push right child onto the stack first so that left child
            # will be popped first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        stack = []
        result = []

        while head or stack:
            if head:
                result.append(head.val)
                if head.right:
                    stack.append(head.right)
                head = head.left
            else:
                head = stack.pop()
        return result
'''