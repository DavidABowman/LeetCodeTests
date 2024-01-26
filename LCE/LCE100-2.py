#Given the roots of two binary trees p and q, 
#write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, 
#and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        #Base Case, if both nodes are none//0, they are the same
        if not p and not q:
            return True
        #If p node is None, and q node is not, they are different
        if not p or not q:
            return False
        #Check if the values of the current nodes are the same
        if p.val != q.val:
            return False
        #Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
'''
class Solution:
    def isSameTree(self, p, q):
        # If both nodes are None, they are identical
        if p is None and q is None:
            return True
        # If only one of the nodes is None, they are not identical
        if p is None or q is None:
            return False
        # Check if values are equal and recursively check left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Values are not equal, they are not identical
        return False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return str(p) == str(q)
'''