# Lab Report — Chapter 4: Quicksort

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your benchmark table — all six rows, including any `RecursionError`.*

```text

```

## Reflection Questions

1. ***Explain quicksort to someone who has never programmed.***
   - **Splitting a pile of papers by last name works. Say what the pivot corresponds to.**
        - *Quicksort is like organizing a messy pile of papers by last name. First, you choose one paper as the pivot, which acts as a reference point. You then divide the other papers into two groups: papers with last names that come before the pivot and papers with last names that come after it. Then, you repeat the same process with each group until all the papers are in the correct order. The pivot helps break a large pile into smaller, easier-to-manage groups.*

2. **A random pivot usually avoids the worst case. Why does randomness help here?**
    - *Using a random pivot helps ensure that the pivot is less likely to be the smallest or largest element in a sorted list. If the pivot is consistently chosen poorly (like always the first or last element), it can lead to unbalanced partitions, which results in the algorithm taking longer to sort (O(n^2) time complexity). Randomly picking a pivot helps create more balanced partitions on average, allowing the algorithm to perform closer to its ideal O(n log n) time complexity.*

3. **Where does sorting show up in software you actually use?**
    - *Sorting is used in many types of software that we use every day. For example, file explorers can sort files by name, date, or size. Online shopping websites can sort products by price, popularity, or ratings. Spreadsheet programs can sort information by different columns, and social media apps can organize posts based on time or relevance. Sorting makes it easier to organize information and find what we need.*
