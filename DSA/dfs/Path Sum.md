https://leetcode.com/problems/path-sum
### Intuition

Simple DFS - recursion.
### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root,targetSum)
    
    def dfs(self, node, rem):
        if not node:
            return False
        if self.isLeaf(node):
            return rem == node.val
        return self.dfs(node.left,rem-node.val) or self.dfs(node.right,rem-node.val)

    def isLeaf(self,node):
        if node == None:
            return False
        return node.left == None and node.right == None
            
```
