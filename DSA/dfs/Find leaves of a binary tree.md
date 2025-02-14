https://leetcode.com/problems/find-leaves-of-binary-tree/

### Intuition
The key insight is that leaves in a binary tree share a common property - they have the same "height" when measured from the bottom up (all leaves are height 1). After removing leaves, new nodes become leaves, and they'll share height 2. This pattern continues until we reach the root. So instead of explicitly removing nodes, we can:

1. Calculate each node's height from bottom-up (max height of children + 1)
2. Group nodes by their height - nodes with same height will be "removed" together
3. Return these groups in order of height (1 to max height)

This turns a seemingly removal-based problem into a height-calculation problem, which is more elegant to implement using DFS.

### Code

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Map<Integer, List<Integer>> heightNodesMap;
    public List<List<Integer>> findLeaves(TreeNode root) {
        // height calc
        // max height
        // 1->maxheight -> add to list (how?)
        // map[height]->nodes having that height
        heightNodesMap = new HashMap<>();
        int maxHeight = getHeight(root);
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=1; i <= maxHeight; i++) {
            ans.add(heightNodesMap.get(i));
        }

        return ans;
    }

    private int getHeight(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int currHeight = Math.max(getHeight(node.left), getHeight(node.right)) + 1;
        if(!heightNodesMap.containsKey(currHeight)) {
            heightNodesMap.put(currHeight,new ArrayList<>());
        }
        heightNodesMap.get(currHeight).add(node.val);
        return currHeight;
    }
}
```
