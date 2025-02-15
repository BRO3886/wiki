https://leetcode.com/problems/clone-graph/description/

### Intuition
The solution uses BFS to traverse the original graph while simultaneously building a clone. It maintains a dictionary `d` where keys are node values and values are the corresponding cloned nodes. As we traverse each node's neighbors, we either create new cloned nodes (if we haven't seen that value before) or reuse existing ones from our dictionary, ensuring we maintain the same connection structure as the original graph.

### Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        d = {}
        root = Node(node.val)
        d[node.val]=root
        q.append(node)
        while len(q) != 0:
            n = q.popleft()
            if n == None:
                continue
            for neighbour in n.neighbors:
                nc = Node(neighbour.val)
                if neighbour.val not in d:
                    d[neighbour.val] = nc
                    q.append(neighbour)
                d[n.val].neighbors.append(d[neighbour.val])
        return root

```