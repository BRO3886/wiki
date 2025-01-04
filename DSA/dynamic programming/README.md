# Dynamic Programming

## What is DP?
Think of DP as "smart recursion with memory". Instead of recalculating the same things again and again, we store results we've already calculated. It's like taking notes while solving a problem so you don't repeat work.

## When to use DP? Look for these hints:
1. "Find maximum/minimum value"
2. "How many ways to..."
3. "Find optimal solution"
4. You see overlapping subproblems (same calculation needed multiple times)

## Systematic Approach for Interviews:
1. Start with Brute Force
   - Write a simple recursive solution first
   - Don't worry about efficiency initially
   - Focus on getting the logic right

2. Identify Overlapping Subproblems
   - What calculations are you doing repeatedly?
   - What information do you need to store?

3. Choose DP Method:
   ```
   a) Top-Down (Memoization)
      - Add a cache to your recursive solution
      - Usually easier in interviews
      - Good when you can't solve all subproblems
   
   b) Bottom-Up (Tabulation)
      - Create a table and fill it iteratively
      - More efficient but harder to write
      - Need to solve all subproblems
   ```

4. Steps for Writing DP in Interview:
   ```
   1. Define state: What information do you need?
   2. Define transition: How do you move to next state?
   3. Define base case: Where does calculation stop?
   4. Define final answer: Which state gives final result?
   ```

Remember: In an interview with limited prep time, starting with top-down (memoization) is usually safer as it's:
1. Closer to brute force solution
2. Easier to explain
3. Easier to debug
