https://leetcode.com/problems/symmetric-tree/

### Intuition

Check both left and right at the same time. Node at the current level should be same and the left and right subtrees should also be same. Simple recursive dfs with a slight modification. In the end if both left and right pointers are null we have reached the end (helps with height check). If either of them is not null it's not balanced.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False
            
            return left.val == right.val and dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)
```