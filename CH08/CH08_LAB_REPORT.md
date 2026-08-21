# Lab Report — Chapter 8: Balanced Trees

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — both tree heights, comparison counts, and the AVL result.*

```text

```

## Reflection Questions

1. ***Explain a binary search tree to someone who has never programmed.***
   - **A "guess higher / guess lower" game works. Say what a node corresponds to.**
        - * A binary search tree (BST) is like a “guess higher or guess lower” game. Each node in the tree represents a value, such as a number. The smaller values are placed on the left side of a node, while larger values are placed on the right side.
        For example, if I am looking for a number, I start at the top node and compare my number to it. If my number is smaller, I go left. If it is larger, I go right. This helps me narrow down the search instead of checking every number one at a time.*
2. ***A tree built from sorted input performs no better than a plain list. Explain why, using your own two trees.***
     * When you insert values into a BST in sorted order (like 1, 2, 3, 4), each new value becomes a right child of the previous one. This results in a tree that looks more like a linked list.* 
          - * Tree A (Mixed Order): This tree is balanced and allows for efficient searching (O(log n)). *
          - * Tree B (Sorted Order): This tree is skewed and behaves like a linked list, leading to inefficient searching (O(n)). Thus, while a BST is generally more efficient than a list, if it's built from sorted input, it loses that efficiency. *

3. **Chapter 8 says balanced trees are used for database indexes. Based on what you built, why is a tree a good fit for that job?**
     - *Balanced trees are a good fit for database indexes because they keep data organized while allowing fast searching, inserting, and deleting. These operations can usually be performed in O(log n) time when the tree remains balanced.
     Trees are also useful because they keep data in an ordered structure. This makes it easier to find specific values or search for a range of values. From building my own trees, I can see why balance is important. A balanced tree stays efficient as more data is added, while an unbalanced tree can become slow and behave more like a list.*
