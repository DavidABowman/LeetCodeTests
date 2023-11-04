#Given the root of a binary tree, return all root-to-leaf paths in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, root: Optional[TreeNode], cur, res) -> None:
        
        # Base Case
        if not root:
            return
        
        # Append node to path
        cur.append(str(root.val))
        
        # If root is a leaf, append path to result
        if not root.left and not root.right:
            res.append('->'.join(cur))
            
        # Recursive Step
        self._dfs(root.left, cur, res)
        self._dfs(root.right, cur, res)
        
        # Backtracking / Post-processing / pop node from path
        cur.pop()
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._dfs(root, [], res)
        return res

        '''          
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
'''