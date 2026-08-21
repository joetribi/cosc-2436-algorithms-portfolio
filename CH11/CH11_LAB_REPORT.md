# Lab Report — Chapter 11: Dynamic Programming

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your call counts, your printed grid, and both string results.*

```text

```

## Reflection Questions

1. ***Explain dynamic programming to someone who has never programmed.***
   - **Writing answers down so you never solve the same problem twice is the core of it.**
        - *Dynamic programming is a method used to solve complex problems by breaking them down into simpler, overlapping subproblems. Imagine you're trying to find the best way to accomplish a task, but some steps repeat themselves. Instead of solving those steps multiple times, you write down the solutions the first time you encounter them and reuse them whenever needed. This approach not only saves time but also ensures that you consistently use the best solutions. Essentially, dynamic programming helps optimize problem-solving by storing intermediate results to avoid redundant calculations.*
2. ***What has to be true about a problem for the grid to work at all?***
   - **Think about what the grid assumes about the subproblems.**
        - *A key requirement for dynamic programming is that the problem must exhibit optimal substructure and overlapping subproblems. This means that the optimal solution to the problem can be constructed from optimal solutions to its subproblems, and the same subproblems are solved multiple times.*
3. ***Where does this show up in real software?***
   - **Spell-check suggestions, `git diff`, DNA sequence comparison — pick one and say how it maps.**
        - *Dynamic programming techniques are prominently used in applications like DNA sequence comparison. For instance, algorithms such as the Smith-Waterman algorithm utilize dynamic programming to find the longest common subsequence between two DNA strands. By breaking the problem down into smaller parts and using a grid to store the results of subproblems, these algorithms can efficiently determine similarities between genetic sequences, which is crucial in bioinformatics for tasks like identifying evolutionary relationships.*
