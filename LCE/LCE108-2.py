#Given an integer array nums where the elements are sorted in ascending order, 
#convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        #Find Middle Index of Array
        mid = len(nums)//2
        #Create Root Node with Mid Element
        root = TreeNode(nums[mid])
        #Recursively Build L&R Subtrees 
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        if not n:
            return None
        
        mid = (n-1)//2
        root = TreeNode(nums[mid])

        root.left = (self.sortedArrayToBST(nums[:mid]))
        root.right = (self.sortedArrayToBST(nums[mid+1:]))
        
        return root
'''