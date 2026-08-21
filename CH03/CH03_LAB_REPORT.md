# Lab Report — Chapter 3: Recursion

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output, including part of the call-stack trace.*

```text

```

## Reflection Questions

1. ***Explain recursion to someone who has never programmed.***
   - **The book uses a box containing boxes. Say what the base case corresponds to.**
      - *Imagine you have a series of boxes stacked inside one another. Each box might contain another box or a small item. To find something in this setup, you would open the outer box, check inside, and if you find another box, you open it too, repeating this process until you reach the smallest box containing the item you are looking for. The "base case" corresponds to the smallest box that either contains the item or is empty, signaling that you cannot go any further.*
2. **An empty folder is a legitimate base case, not an error. Why does treating it as an error break the program?**
   - *An empty folder is a valid result because there is simply nothing inside it to search. The program should be able to recognize this and return a result such as 0. If the program treats an empty folder as an error, it may stop unexpectedly or give an incorrect result instead of continuing normally. This can interfere with the recursion and cause the program to work incorrectly.*
3. **A folder nested 10,000 levels deep would crash your code. Why?**
   - *A folder nested 10,000 levels deep would require the recursive function to call itself thousands of times. Python has a limit on how many recursive calls can be made, usually around 1,000. Going beyond this limit causes a RecursionError because each function call uses space in the call stack. Once the stack reaches its limit, Python stops the program to prevent further problems.*
