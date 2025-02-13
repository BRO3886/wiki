### Intuition
Use `visited[][]` array to mark cells we're currently using in our path `(visited[i][j] = true)`, explore all possible directions, then unmark them `(visited[i][j] = false)` when backtracking to try different paths. This prevents reusing cells within the same path while allowing them to be used in new attempts.

### Code

```java
class Solution {
    // Direction arrays for moving up, down, left, right
    private static final int[] DX = {1, -1, 0, 0};
    private static final int[] DY = {0, 0, 1, -1};
    
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];
        
        // Try each cell as a starting point
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word.charAt(0) && searchWord(i, j, 0, word, visited, board)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    private boolean searchWord(int row, int col, int index, String word, 
                             boolean[][] visited, char[][] board) {
        // Base case: found the complete word
        if (index == word.length()) {
            return true;
        }
        
        // Check boundaries and validation
        if (!isValid(row, col, board) || 
            visited[row][col] || 
            board[row][col] != word.charAt(index)) {
            return false;
        }
        
        // Mark current cell as visited
        visited[row][col] = true;
        
        // Explore all four directions
        for (int i = 0; i < 4; i++) {
            int newRow = row + DX[i];
            int newCol = col + DY[i];
            
            if (searchWord(newRow, newCol, index + 1, word, visited, board)) {
                visited[row][col] = false;  // Clean up before returning
                return true;
            }
        }
        
        // Backtrack
        visited[row][col] = false;
        return false;
    }
    
    private boolean isValid(int row, int col, char[][] board) {
        return row >= 0 && row < board.length && col >= 0 && col < board[0].length;
    }
}
```

### Time Complexity
 O(N * M * 4^L) where:
- N = number of rows in board
- M = number of columns in board
- L = length of word
- 4 represents the four directions we can move at each step