"""
Lab: "Cheapest Route" -- Weighted Graphs and Dijkstra's Algorithm

Part 1: Implement Dijkstra's algorithm (dict-of-dicts weighted graph).
Part 2: Compare BFS "fewest hops" vs Dijkstra "lowest cost" on a small
        San Francisco style map (Twin Peaks -> Golden Gate Bridge).
Part 3: Break Dijkstra's algorithm on purpose with a negative-weight edge.

All graphs below are hardcoded literals -- no randomness, no file I/O --
so the autograder can check exact costs, parents, and paths.
"""

from collections import deque

INFINITY = float("inf")


# ---------------------------------------------------------------------------
# PART 1: Weighted graphs and Dijkstra's algorithm
# ---------------------------------------------------------------------------

def find_lowest_cost_node(costs, processed):
    lowest_cost = INFINITY
    lowest_cost_node = None
    
    for node, cost in costs.items():
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
            
    return lowest_cost_node


def dijkstra(graph, start, finish):
    costs = {}
    parents = {}
    processed = []

    # Step 1: Initialize costs and parents
    for node in graph:
        costs[node] = INFINITY
        parents[node] = None
    costs[start] = 0

    # Step 2: Update costs and parents for direct neighbors of start
    for neighbor, weight in graph[start].items():
        costs[neighbor] = weight
        parents[neighbor] = start

    # Step 3: Find the lowest cost node
    node = find_lowest_cost_node(costs, processed)

    # Step 4: Process nodes until there are none left
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor, weight in neighbors.items():
            new_cost = cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    return costs, parents


def build_path(parents, start, finish):
    path = []
    node = finish

    while node is not None:
        path.append(node)
        node = parents.get(node)

    path.reverse()
    return path


# Book's warm-up graph: Start / A / B / Finish (dict-of-dicts)
book_graph = {}
book_graph["start"] = {"a": 6, "b": 2}
book_graph["a"] = {"finish": 1}
book_graph["b"] = {"a": 3, "finish": 5}
book_graph["finish"] = {}


# ---------------------------------------------------------------------------
# PART 2: Fewest hops vs. lowest cost (Twin Peaks -> Golden Gate Bridge)
# ---------------------------------------------------------------------------

def bfs_shortest_path(graph, start, finish):
    """
    Provided from Chapter 6: breadth-first search finds the path with the
    FEWEST EDGES (hops) on an unweighted graph (dict-of-lists). This
    function is already implemented for you -- study it, don't edit it.
    """
    queue = deque([start])
    visited = set([start])
    parents = {start: None}

    while queue:
        node = queue.popleft()
        if node == finish:
            break
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = node
                queue.append(neighbor)

    path = []
    node = finish
    while node is not None:
        path.append(node)
        node = parents.get(node)
    path.reverse()
    return path




# Unweighted version (dict-of-lists) -- same map, ignoring travel time.
sf_unweighted = {
    "twin_peaks": ["a", "c"],
    "a": ["b"],
    "b": ["golden_gate"],
    "c": ["d"],
    "d": ["e"],
    "e": ["golden_gate"],
    "golden_gate": [],
}

# Weighted version (dict-of-dicts) -- edge weights are travel time.
# The 3-segment route (twin_peaks -> a -> b -> golden_gate) is SLOWER
# than the 4-segment route (twin_peaks -> c -> d -> e -> golden_gate).
sf_weighted = {
    "twin_peaks": {"a": 10, "c": 3},
    "a": {"b": 10},
    "b": {"golden_gate": 10},
    "c": {"d": 3},
    "d": {"e": 3},
    "e": {"golden_gate": 3},
    "golden_gate": {},
}


# ---------------------------------------------------------------------------
# PART 3: Break Dijkstra's algorithm on purpose (negative-weight edge)
# ---------------------------------------------------------------------------

# Trade graph with a negative-weight edge (a -> b costs -10). The TRUE
# cheapest route start -> a -> b -> finish costs 2 + (-10) + 5 = -3, but
# because start -> b (1) looks cheaper than start -> a (2) up front,
# Dijkstra's algorithm marks "b" as processed BEFORE it discovers the
# negative edge through "a" -- so the reported cost to "finish" ends up
# stale and wrong.
trade_graph = {}
trade_graph["start"] = {"a": 2, "b": 1}
trade_graph["a"] = {"b": -10}
trade_graph["b"] = {"finish": 5}
trade_graph["finish"] = {}


if __name__ == "__main__":
    print("=== Part 1: Book's warm-up graph ===")
    costs, parents = dijkstra(book_graph, "start", "finish")
    print("Costs:", costs)
    print("Parents:", parents)
    path = build_path(parents, "start", "finish")
    print("Path:", " -> ".join(path))
    print()

    print("=== Part 2: Twin Peaks -> Golden Gate Bridge ===")
    hops_path = bfs_shortest_path(sf_unweighted, "twin_peaks", "golden_gate")
    print("BFS fewest-hops path:", " -> ".join(hops_path))
    print("BFS hop count:", len(hops_path) - 1)

    sf_costs, sf_parents = dijkstra(sf_weighted, "twin_peaks", "golden_gate")
    cheapest_path = build_path(sf_parents, "twin_peaks", "golden_gate")
    print("Dijkstra lowest-cost path:", " -> ".join(cheapest_path))
    print("Dijkstra total cost:", sf_costs["golden_gate"])
    # BFS answers "fewest segments"; Dijkstra answers "lowest total weight."
    # Here they disagree: BFS's 3-segment route is actually the SLOWER one.
    print()

    print("=== Part 3: Breaking Dijkstra with negative weights ===")
    trade_costs, trade_parents = dijkstra(trade_graph, "start", "finish")
    print("Costs:", trade_costs)
    print("Parents:", trade_parents)
    trade_path = build_path(trade_parents, "start", "finish")
    print("Path:", " -> ".join(trade_path))
    print("Reported cost to finish:", trade_costs["finish"])
    print("True cheapest cost (by hand): 2 + (-10) + 5 = -3")
    # Hand-trace: "b" gets marked processed at cost 1 (direct edge from
    # start) before Dijkstra ever explores "a" -> "b" at -10. Once "b" is
    # processed, its own neighbor "finish" is never re-relaxed with the
    # cheaper value discovered later, so costs["finish"] stays stale.
    # The broken assumption: Dijkstra assumes a processed node's cost can
    # never improve later, which negative weights violate. Bellman-Ford
    # is the algorithm that correctly handles negative-weight edges.
