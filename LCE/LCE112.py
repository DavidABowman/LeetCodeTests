#Given the root of a binary tree and an integer targetSum,
#return true if the tree has a root-to-leaf path
#such that adding up all the values along the path equals targetSum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,s):
            if not node:
                return
            s += (node.val)
            if node.left is None and node.right is None:
                if s == targetSum:
                    return True
            return dfs(node.left,s) or dfs(node.right,s)
        return dfs(root,0)