#Given a binary tree, find its minimum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            current_node, depth = queue.popleft()
            #Check if current node is a leaf node
            if not current_node.left and not current_node.right:
                return depth
            #Enqueue the children of the current node
            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        elif not root.right and not root.left: return 1
        elif not root.right: return 1 + self.minDepth(root.left)
        elif not root.left: return 1 + self.minDepth(root.right)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth 
            return min(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
'''
