# Lab Report — Chapter 6: Breadth-First Search

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output for all three searches — reachable, distance, and full path.*

```text

```

## Reflection Questions

1. ***Explain breadth-first search to someone who has never programmed.***
   - **Asking your friends, then their friends, is exactly it. Say what the queue corresponds to.**
        * Breadth-First Search (BFS) is like asking your friends about their friends. Imagine you're trying to find out who knows a specific skill. You start with yourself, ask your friends, and then ask their friends. This way, you explore all connections at one level before moving deeper.*

2. **Two people in your network each know the other. Walk through what happens without the `searched` set.**
    - *Without using a 'searched' set, if both "you" and "alice" know "bob," the search could get stuck in a loop. For example, if you start asking "you," you might ask "alice," who then directs you back to "bob." If you then ask "bob," he directs you back to "you." This cycle continues endlessly, and you never reach new connections because you keep revisiting the same people.*

3. ***Where does this show up in real software?***
   - **"People you may know," shortest routes, network hops — pick one and say how it maps.**
        - *A common application of BFS is in social networking platforms like Facebook. In the "People You May Know" feature, the algorithm explores your immediate connections (friends) and then their connections (friends of friends) to suggest new connections. This approach efficiently identifies potential new friends based on mutual connections.*
