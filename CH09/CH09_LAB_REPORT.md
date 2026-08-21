# Lab Report — Chapter 9: Dijkstra's Algorithm

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — the costs table, the parents table, the path, and the
negative-weight result.*

```text

```

## Reflection Questions

1. ***Explain Dijkstra's algorithm to someone who has never programmed.***
   - **Planning a drive with traffic, or the book's piano trade, both work.**
      - *Dijkstra's algorithm can be thought of as a way to find the shortest path between two points, like planning a drive from your home to a friend's house while avoiding traffic. Imagine you have a map with various routes and each route has a different travel time. Dijkstra's algorithm helps you find the quickest route by looking at all possible paths and choosing the one that takes the least time. It does this step by step, always picking the route that currently seems the fastest, and then updating its choices as it learns more about the other routes.*

2. **Why does the algorithm always pick the cheapest unprocessed node next, instead of going in order?**
   - *The algorithm picks the cheapest unprocessed node next because it operates on a principle known as "greedy choice." By always selecting the node with the lowest cost, it ensures that every decision made is optimal at that moment. This strategy allows the algorithm to efficiently explore the graph and guarantees that once a node is processed (meaning its shortest path is finalized), it will not be revisited. If it were to go in order, it might miss the optimal paths that could be discovered through less direct routes.*

3. **Where does the "cost" on an edge come from in real routing software, and how does changing what you measure change the answer without changing the algorithm?**
   - *In real routing software, the "cost" on an edge often represents factors like distance, travel time, tolls, or even traffic conditions. For example, a highway might have a lower cost in terms of travel time compared to a back road, even if the distance is similar. Changing what you measure—say, from travel time to distance—would alter the edge weights in the graph. However, Dijkstra's algorithm itself remains unchanged; it will still find the shortest path based on the new costs. This flexibility allows the algorithm to be adapted for different scenarios, like finding the quickest or the shortest route depending on the needs of the user. Feel free to ask if you need further clarification on any of these points!*
