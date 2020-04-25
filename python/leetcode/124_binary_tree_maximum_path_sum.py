#%%
"""
- Binary Tree Maximum Path Sum
- https://leetcode.com/problems/binary-tree-maximum-path-sum/
- Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""

#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#%%
class S1:

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.global_max = root.val if root else 0
        self.findmax(root)
        return self.global_max

    def findmax(self, node):
        if not node:
            return 0
        
        left = self.findmax(node.left)
        left = left if left > 0 else 0

        right = self.findmax(node.right)
        right = right if right > 0 else 0

        self.global_max = max(left + right + node.val, self.global_max)
        return max(left, right) + node.val
