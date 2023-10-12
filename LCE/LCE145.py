#Given the root of a binary tree, return the postorder traversal of its nodes' values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        # Base case...
        if not root: return []
        # Create an array list to store the solution result...
        sol = []
        # Create an empty stack and push the root node...
        bag = [root]
        # Loop till stack is empty...
        while bag:
            # Pop a node from the stack...
            node = bag.pop()
            sol.append(node.val)
            # Push the left child of the popped node into the stack...
            if node.left:
                bag.append(node.left)
            # Append the right child of the popped node into the stack...
            if node.right:
                bag.append(node.right)
        return sol[::-1]       # Return the solution list...
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tail = root
        stack = []
        result = []

        while tail or stack:
            if tail:
                result.append(tail.val)
                if tail.left:
                    stack.append(tail.left)
                tail = tail.right
            else:
                tail = stack.pop()
        return result
'''