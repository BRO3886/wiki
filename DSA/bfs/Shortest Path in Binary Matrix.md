https://leetcode.com/problems/shortest-path-in-binary-matrix/

### Intuition
This is a classic BFS approach that explores the matrix **level by level**, where each level represents cells that are the same distance from the start. By using a queue and visiting cells in order of increasing distance (1 step, then 2 steps, etc.), the first time we reach the target cell (n-1, n-1) is guaranteed to be via the shortest possible path (how? level by level). We use a visited array to avoid cycles and track each cell's distance from start in the queue.

### Code

```java
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if(grid[0][0] != 0 || grid[n-1][n-1] != 0) {
            return -1;
        }
        
        Queue<int[]> q = new LinkedList();
        int[][] dxs = {
            {1,0},{-1,0},{0,1},{0,-1},
            {-1,-1},{1,1},{-1,1},{1,-1}
        };
        boolean[][] visited = new boolean[n][n];

        q.add(new int[]{0,0,1});
        visited[0][0] = true;
        while(!q.isEmpty()) {
            int[] data = q.poll();
            int i = data[0];
            int j = data[1];
            int dist = data[2];

            if (i == n-1 && j == n-1) {
                return dist;
            }

            for (int[] d: dxs) {
                int ni = i+d[0];
                int nj = j+d[1];
                if (inLimits(ni,nj,n) && grid[ni][nj] == 0 && !visited[ni][nj]) {
                    visited[ni][nj] = true;
                    q.add(new int[]{ni,nj,dist+1});
                }
            }
        }
        return -1;
    }

    private boolean inLimits(int i, int j, int n) {
        if (i < 0) {
            return false;
        }

        if (j < 0) {
            return false;
        }

        if (i >= n) {
            return false;
        }

        if (j >= n) {
            return false;
        }

        return true;
    }
}
```

