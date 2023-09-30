#Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        
        while root or stack:
          while root:
            stack.append(root)
            root = root.left
          root = stack.pop()
          result.append(root.val)
          root = root.right
        return result
    
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return  inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
'''