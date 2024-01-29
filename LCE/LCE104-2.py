#Given the root of a binary tree, return its maximum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Base Case: if node = none, return 0
        if not root:
            return 0
        #Recursively calculate depth of L&R subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        #Return MaxDepth among L&R subtrees, plus 1 for current node
        return max(left_depth, right_depth) + 1
        
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)

#Tried Recursive Solution - I messed it up tho :(
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.left = maxDepth(root.left)
        self.right = maxDepth(root.right)
        return 1 + max(self.left, self.right)
'''