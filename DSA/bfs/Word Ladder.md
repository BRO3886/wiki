
A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return _the **number of words** in the **shortest transformation sequence** from_ `beginWord` _to_ `endWord`_, or_ `0` _if no such sequence exists._

**Example 1:**
```
**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**Output:** 5
**Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

```

**Example 2:**
```
**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**Output:** 0
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

**Constraints:**
- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are **unique**.
### Intuition

The solution uses BFS where we process words level by level to find the shortest transformation sequence. The size = q.size() captures all words at the current transformation level, ensuring we process all possible one-letter changes for those words before moving to the next level. This level-by-level processing helps us track the minimum number of transformations needed to reach the target word.

### Code

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> q = new LinkedList<>();
        Set<String> s = new HashSet<>();
        for (String w: wordList) {
            s.add(w);
        }

        if (!s.contains(endWord)) {
            return 0;
        }

        q.add(beginWord);
        int count = 1;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                String curr = q.poll();
                if (curr.equals(endWord)) {
                    return count;
                }

                char[] arr = curr.toCharArray();
                for (int i = 0; i < curr.length(); i++) {
                    for (char c= 'a'; c <= 'z'; c++) {
                        char temp = arr[i];
                        arr[i] = c;
                        String newWord = new String(arr);
                        if (s.contains(newWord)) {
                            q.add(newWord);
                            s.remove(newWord);
                        }
                        arr[i] = temp;
                    }
                }
            }
            count++;
        }
        return 0;
    }
}
```

