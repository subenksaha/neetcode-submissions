# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, n):
            if not curr: return n
            n += 1
            l = dfs(curr.left, n)
            r = dfs(curr.right, n)
            
            max_ = max(l,r)
            return max_
        return dfs(root, 0)