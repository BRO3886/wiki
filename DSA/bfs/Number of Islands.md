https://leetcode.com/problems/number-of-islands/description/

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
**Example 1:**

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

**Example 2:**

**Input:** grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
**Output:** 3

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

### Intuition
simple DFS or BFS

```java
class Pair {
    int row, col;
    Pair(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

class Solution {
    char[][] grid;
    boolean[][] visited;
    int m, n;
    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.m = this.grid.length;
        this.n = this.grid[0].length;
        this.visited = new boolean[m][n];
        int count=0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !this.visited[i][j]) {
                    this.visited[i][j] = true;
                    bfs(i, j);
                    count++;
                }
            }
        }

        return count;
    }

    private void bfs(int i, int j) {
        Queue<Pair> q = new LinkedList();
        q.add(new Pair(i,j));
        int[] dRow = {-1, 1, 0, 0};
        int[] dCol = {0, 0, -1, 1};
        while (!q.isEmpty()) {
            Pair p = q.poll();
            int r = p.row, c = p.col;
            for (int itr = 0; itr < 4; itr++) {
                int nr = r + dRow[itr];
                int nc = c + dCol[itr];

                if (nr >=0 && nr < this.m && nc >= 0 && nc < this.n && grid[nr][nc] == '1' && visited[nr][nc] == false ) {
                    q.add(new Pair(nr, nc));
                    this.visited[nr][nc] = true;
                }
            }
        }
    }
}
```