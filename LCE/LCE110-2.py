#Given a binary tree, determine if it is height-balanced
#A height-balanced binary tree is a binary tree in which the depth 
#of the two subtrees of every node never differs by more than one.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            #Check if L&R Subtrees are Balanced
            is_current_balanced = abs(left_height - right_height) <= 1
            #Check if Current Subtree is Balanced
            is_current_balanced = is_current_balanced and left_balanced and right_balanced
            #Return Height and Balanced Status of Current Subtree
            return max(left_height, right_height) + 1, is_current_balanced 
        _, result = check_balance(root)
        return result
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:  return 0
        leftHeight, rightHeight = self.Height(root.left), self.Height(root.right)
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:  return -1
        return max(leftHeight, rightHeight) + 1
'''