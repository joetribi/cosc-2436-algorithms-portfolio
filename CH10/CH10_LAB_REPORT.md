# Lab Report — Chapter 10: Greedy Algorithms

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your scheduling result, both knapsack answers side by side, your set cover, and your subset counts.*

```text

```

## Reflection Questions

1. ***Explain the greedy strategy to someone who has never programmed.***
  - **Packing a suitcase, or filling a schedule, both work.**
    - *The greedy strategy is like making decisions based on the best option available at the moment, without worrying about the future consequences. For example, when packing a suitcase, you might choose to put in the heaviest items first, thinking that they take up the most space and are the most important. Similarly, when filling a schedule, you select the activities that fit best in the available time slots, aiming to maximize what you can accomplish without considering how it might affect your choices later.*
2. **Greedy was perfect for scheduling and wrong for the knapsack. What changed about the problem?**
  - *The key difference lies in the nature of the problems. In scheduling, the goal is to maximize the number of non-overlapping classes. The greedy approach works perfectly because choosing the class that ends the soonest allows for the most possible classes to fit in the schedule. However, in the knapsack problem, the goal is to maximize the total value of items within a weight limit. Greedily selecting the highest value items can lead to suboptimal choices, as it may overlook combinations of lower-value items that could yield a higher total value within the weight limit.*
3. **You already wrote a greedy algorithm in an earlier lab — building the Huffman tree in Chapter 7 repeatedly merges the two lowest-frequency nodes. Is that one exactly optimal, or an approximation?**
  - *In Chapter 7, we used a greedy algorithm to build the Huffman tree by repeatedly merging the two lowest-frequency nodes. This algorithm is exactly optimal because it ensures the most efficient encoding for symbols based on their frequencies. By giving shorter codes to more common symbols and longer codes to rarer ones, it minimizes the average code length. In our lab, we also explored other greedy strategies. For example, classroom scheduling uses a greedy approach that guarantees the maximum number of non-overlapping classes. However, the greedy strategy for the 0/1 knapsack problem can lead to suboptimal results, as it might miss better combinations of items. Similarly, the greedy set-covering algorithm provides an approximation rather than an exact solution. Thus, while the Huffman algorithm is a greedy strategy that guarantees an optimal solution, not all greedy algorithms yield the same level of effectiveness.*
