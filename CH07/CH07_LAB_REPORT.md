# Lab Report — Chapter 7: Trees and Huffman Coding

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your BFS and DFS orders, your encode/decode round trip, and your bit counts.*

```text

```

## Reflection Questions

1. ***Explain the difference between BFS and DFS to someone who has never programmed.***
   - **Searching a building floor by floor, versus following one hallway to its end.**
      - *Breadth-First Search (BFS): Imagine you are searching a building floor by floor. You check all the rooms on one floor before moving up to the next floor. This means you explore all nodes at the present depth level before moving on to nodes at the next depth level.*
      - *Depth-First Search (DFS): Think of it as following one hallway to its end before moving to another. You go as deep as possible down one path (or node) before backtracking. This results in exploring one branch fully before moving to another.*
2. **Why do frequent letters get shorter codes? Use your own code table.**
   - *Frequent letters get shorter codes because of how Huffman coding works. The algorithm assigns shorter binary codes to characters that appear more frequently, optimizing space. Example Code Table:
      Let's say we have "abracadabra":
      a: 5
      b: 2
      r: 2
      c: 1
      d: 1
      The Huffman coding might assign:
      a: 0
      b: 10
      r: 11
      c: 110
      d: 111*

3. **Your decoder reads a stream of bits with no separators and still gets it right. Why is there never any ambiguity?**
   - *The reason there is never any ambiguity in decoding is that Huffman coding generates a uniquely decodable prefix code. This means that no code is a prefix of any other code, allowing the decoder to read a stream of bits without confusion. For example, using the "abracadabra" codes:
   If the encoded string is 0101100110010110, the decoder will always know where one character ends, and the next begins, because no code starts with the same bits as another.
