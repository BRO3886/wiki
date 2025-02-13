Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in  `t`  (**including duplicates**) is included in the window. If there is no such substring, return _the empty string_ `""`.

The testcases will be generated such that the answer is **unique**.

```
**Example 1:**

**Input:** s = "ADOBECODEBANC", t = "ABC"
**Output:** "BANC"
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**

**Input:** s = "a", t = "a"
**Output:** "a"
**Explanation:** The entire string s is the minimum window.

**Example 3:**

**Input:** s = "a", t = "aa"
**Output:** ""
**Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` and `t` consist of uppercase and lowercase English letters.


### Intuition
The solution uses a sliding window with two pointers (`begin` and `end`) and a counter mechanism. The right pointer expands to find valid windows (when counter hits 0, meaning we found all characters from t), while the left pointer contracts to optimize these valid windows. What's unique is that optimization happens inside the counter == 0 loop because we can keep finding better (smaller) valid windows by removing characters from the start as long as our window remains valid. The character frequency map handles both finding and maintaining window validity, especially for duplicate characters.
### Code
```java
class Solution {
    public String minWindow(String s, String t) {
        int[] charCount = new int[128];
        for (char c: t.toCharArray()) {
            charCount[c]++;
        }

        int start = 0;
        int end = 0;
        int counter = t.length();
        String ans = "";
        int minLen = Integer.MAX_VALUE;
        while(end < s.length()) {
            char c = s.charAt(end);
            charCount[c]--;
            if (charCount[c] >= 0) {
                counter--;
            }
            
            while(counter == 0) {                
                if (end - start + 1 < minLen) {
                    minLen = end - start + 1;
                    ans = s.substring(start, end+1);
                }

                char st = s.charAt(start);
                charCount[st]++;
                if (charCount[st] > 0) {
                    counter++;
                }
                start++;
            }
            end++;
        }

        return ans;
    }
}
```