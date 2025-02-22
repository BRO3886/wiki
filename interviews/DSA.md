questions on DSA

6/1/25
[LC 210 - Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)
Tags: [[Graphs]], [[BFS]]

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where `prerequisites[i] = [ai, bi]` indicates that you must take course bi first if you want to take course ai.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


8/1/25
[LC 212 - Word Search II](https://leetcode.com/problems/word-search-ii/description/)
Tags: [[Trie]], [[DFS]]

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

```python
from typing import List, Set


class Node:
    def __init__(self, letter: str):
        self.letter = letter
        self.next = {}
        self.end = False

    def add_node(self, node):
        self.next = node

    def __str__(self):
        print(f"{self.letter}")

    def exists(self, letter: str):
        return letter in self.next

    def mark_end(self):
        self.end = True


def insert(root: Node, word: str):
    temp = root
    for letter in word:
        if not temp.exists(letter):
            temp.next[letter] = Node(letter)
        temp = temp.next[letter]
    temp.mark_end()


def solution(matrix: List[List[str]], words: List[str], m: int, n: int) -> List[str]:
    # 1. create trie
    # 2. iterate through the matrix
    # 3. on finding starting point of word, follow through the matrix
    # TC
    # 1. trie creation: O(words * len)
    # 2. matrix iteration: O(m * n)
    # 3. node lookup: O(1) (dict)
    root = Node("-")
    for word in words:
        insert(root, word)

    return find_words(matrix, root, m, n)


def find_words(matrix: List[List[str]], root: Node, m: int, n: int) -> List[str]:
    ans = []
    for i in range(m):
        for j in range(n):
            letter = matrix[i][j]
            if root.exists(letter):
                helper(matrix, i, j, m, n, root.next[letter], ans, "" + letter)

    return ans


def helper(
    matrix: List[List[str]],
    i: int,
    j: int,
    m: int,
    n: int,
    node: Node,
    ans: List[str],
    word: str,
):
    if node.end:
        ans.append(word)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < m and 0 <= y < n:
            letter = matrix[x][y]
            if node.exists(letter):
                helper(
                    matrix, x, y, m, n, node.next[letter], ans, word + letter
                )


ans = solution(
    [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    ["oath", "pea", "eat", "rain"],
    4,
    4,
)

print(ans)

ans = solution(
    [["a", "b"], ["c", "d"]],
    ["abcb"],
    2,
    2,
)

print(ans)
```


Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.


Problem 2: 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. 
You must solve this problem without using the library's sort function. 
