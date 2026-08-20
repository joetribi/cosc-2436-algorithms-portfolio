# Lab Report — Chapter 1: Binary Search

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your printed step counts and describe what your growth chart shows.*

```text

```

## Reflection Questions

1. ***Explain binary search to someone who has never programmed.***
     - **The book uses looking up a name in a phone book. Say what corresponds to what.**
        - *Imagine you are looking for a name in a phone book. Instead of starting at the first name, you open the book in the middle. If the name you want comes before it, you search the first half; if it comes after, you search the second half. This process of dividing the search area in half continues until you find the name or determine that it’s not in the book. This is called binary search, which is much faster than checking each name one by one.*

2. ***Doubling the list adds only one step to binary search. Why does that happen?***
     - **Answer from what your code does each guess, not from a formula.**
        - *In binary search, each guess eliminates half of the remaining items. When you double the list size, the number of steps only increases by one because you are still halving the search space with each step. For example, if it takes 10 steps to find an item in a list of size 1024, it will take 11 steps for a list of size 2048.*

3. **Where does binary search show up in real software?**
      - Binary search is commonly used in applications that require efficient searching through sorted data, such as database search algorithms, library catalogs, and e-commerce websites.*
