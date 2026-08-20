# Lab Report — Chapter 2: Selection Sort

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your sorted lists and your ranked artist output.*

```text

```

## Reflection Questions

1. ***Explain selection sort to someone who has never programmed.***
   - **Sorting a hand of cards, or picking players for a team, both work.**
        - *Selection sort can be compared to sorting a hand of cards. Imagine you have a shuffled deck, and you want to arrange it by rank. You would look through your cards, find the lowest rank, and place it in a new pile. Then, you repeat this process for the remaining cards until all are sorted. It is like picking players for a team; you choose the best available player first and continue until all positions are filled.*

2. ***Your list gets twice as long. Does selection sort do twice the work, or more?***
   - **Answer from what your code does — how many passes, and how much each pass looks at.**
        - *It does more than twice the work. The program checks the remaining items on each pass to find the smallest one. When the list gets bigger, there are more items to check on every pass.*

3. **Chapter 2 says arrays are used more often than linked lists in practice. Based on what you built, why would that be?**
    - *Arrays are generally preferred over linked lists because they allow for faster access to elements. In an array, you can access any element directly using its index, which takes constant time (O(1)). In contrast, linked lists require traversal from the head to reach a specific element, which takes linear time (O(n)). Additionally, arrays have better cache locality, leading to improved performance in practice, especially for algorithms that require frequent access to elements, like selection sort.*
