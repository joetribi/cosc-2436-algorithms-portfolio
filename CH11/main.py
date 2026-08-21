"""
Lab: "Write It Down Once" -- Dynamic Programming

Part 1: Measure the waste (naive recursive knapsack + call counter)
Part 2: Fill the grid instead (bottom-up DP knapsack)
Part 3: Point the same technique somewhere else (longest common
        substring vs longest common subsequence)

All data below is hardcoded -- no randomness, no file I/O.
The naive recursion is capped at 18 items so it finishes well inside
the autograder's time budget (2**18 is roughly half a million calls).
"""


# ---------------------------------------------------------------------------
# Part 1: Measure the waste
# ---------------------------------------------------------------------------

def naive_knapsack(items, capacity, index, counter):
    """
    Naive recursive 0/1 knapsack: at each item, either take it or don't,
    and return the best value achievable from items[index:] given the
    remaining capacity.

    items: list of (weight, value) tuples
    capacity: remaining capacity (int)
    index: index of the current item being considered
    counter: a one-element list, e.g. [0], used to count every call
             made to this function (increment counter[0] each call)

    Returns: best value achievable (int)
    """
    # TODO: increment counter[0] to record that this call happened

    # TODO: implement the base case -- no items left to consider, or
    #       capacity has run out

    # TODO: implement the recursive case -- compute the best value if we
    #       skip items[index], and (if it fits) the best value if we take
    #       items[index]; return the larger of the two

    # Record that this call happened.
    counter[0] += 1

    # Base case: no items left to consider, or capacity has run out.
    if index >= len(items) or capacity <= 0:
        return 0

    weight, value = items[index]

    # Option 1: skip this item.
    without_item = naive_knapsack(items, capacity, index + 1, counter)

    # Option 2: take this item, if it fits.
    if weight <= capacity:
        with_item = value + naive_knapsack(items, capacity - weight, index + 1, counter)
        return max(without_item, with_item)

    return without_item



# ---------------------------------------------------------------------------
# Part 2: Fill the grid instead
# ---------------------------------------------------------------------------

def dp_knapsack(items, capacity):
    """
    Bottom-up dynamic programming knapsack.

    Build a grid with one row per item (plus a row 0 for "no items yet")
    and one column per capacity value from 0 to capacity.

    # TODO: in a comment right here, write ONE complete sentence describing
    #       what grid[i][j] means. For example (write your own words):
    #       "grid[i][j] is ______________________________________________"

    Returns: (grid, best_value) where grid is a list of lists and
             best_value is the value in the bottom-right cell.
    """
    rows = len(items) + 1
    cols = capacity + 1

    # Build the grid as a list of lists, rows x cols, initialized to 0.
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Fill the grid row by row using the knapsack recurrence:
    # grid[i][j] = best value using items up to row i with capacity j
    # (either skip item i-1, or take it if it fits).
    for i in range(1, rows):
        weight, value = items[i - 1]
        for j in range(cols):
            without_item = grid[i - 1][j]
            if weight <= j:
                with_item = value + grid[i - 1][j - weight]
                grid[i][j] = max(without_item, with_item)
            else:
                grid[i][j] = without_item

    best_value = grid[rows - 1][cols - 1]
    return grid, best_value


def print_grid(grid):
    """
    Print the grid in a readable, row-by-row format so students can
    actually look at the values that were computed.
    """
    # TODO: loop over each row in grid and print it in a readable way
    for row_index, row in enumerate(grid):
        print("row {}: {}".format(row_index, row))


# ---------------------------------------------------------------------------
# Part 3: Point the same technique somewhere else
# ---------------------------------------------------------------------------

def longest_common_substring(a, b):
    """
    Return the longest common SUBSTRING of a and b (letters must be
    consecutive in both strings).

    Build a grid where grid[i][j] is 0 on a mismatch between a[i-1] and
    b[j-1], and grid[i-1][j-1] + 1 on a match. Track the largest value
    seen anywhere in the grid and the substring that produced it.
    """
    # TODO: build the grid (len(a)+1 rows, len(b)+1 columns) initialized to 0

    # TODO: fill the grid using the substring recurrence described above,
    #       keeping track of the maximum value found and its ending position

    # TODO: use the tracked max length/position to slice out the actual
    #       longest common substring from a (or b)

    rows = len(a) + 1
    cols = len(b) + 1
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    max_len = 0
    end_index = 0  # index in a where the best match ends

    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
                if grid[i][j] > max_len:
                    max_len = grid[i][j]
                    end_index = i
            else:
                grid[i][j] = 0

    # Slice out the actual longest common substring using the tracked
    # max length and ending position.
    return a[end_index - max_len:end_index]



def longest_common_subsequence(a, b):
    """
    Return the longest common SUBSEQUENCE of a and b (letters do NOT need
    to be consecutive, just in the same relative order).

    Same grid shape as longest_common_substring, but a different rule:
    on a match, grid[i][j] = grid[i-1][j-1] + 1; on a mismatch,
    grid[i][j] = max(grid[i-1][j], grid[i][j-1]).
    """
    # TODO: build the grid (len(a)+1 rows, len(b)+1 columns) initialized to 0

    # TODO: fill the grid using the subsequence recurrence described above

    # TODO: walk back through the grid (or otherwise reconstruct) to build
    #       the actual longest common subsequence string

    rows = len(a) + 1
    cols = len(b) + 1
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

    # Walk back through the grid to reconstruct the actual subsequence.
    i, j = rows - 1, cols - 1
    result = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif grid[i - 1][j] >= grid[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return "".join(result)

# ---------------------------------------------------------------------------
# Entry point -- hardcoded, deterministic scaffolding
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # 20 hardcoded (weight, value) items. Naive recursion is capped at the
    # first 18 of these to stay inside the autograder's time budget.
    items = [
        (2, 3), (3, 4), (4, 5), (5, 6), (9, 10),
        (1, 1), (6, 7), (7, 8), (8, 9), (10, 11),
        (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
        (7, 7), (8, 8), (9, 9), (10, 10), (1, 2),
    ]
    capacity = 50

    print("Part 1: Measure the waste")

    # Run the naive recursion on growing subsets of items: 3, 10, 18.
    # (Not 20 -- 18 keeps 2**n calls around half a million, well inside
    # the 15-second test budget; 20+ would risk blowing it.)
    last_naive_count = 0
    for n in [3, 10, 18]:
        subset = items[:n]
        counter = [0]
        naive_knapsack(subset, capacity, 0, counter)
        print(n)
        print(counter[0])
        last_naive_count = counter[0]

    # Growth pattern observed: each time we add roughly the same number of
    # extra items, the call count roughly doubles per added item -- the
    # naive recursion explores 2 choices (take/skip) per item, so the
    # total number of calls grows like 2**n. This is the same doubling
    # pattern we measured with quicksort back in Chapter 4, except this
    # time it is working against us instead of for us.

    print()
    print("Part 2: Fill the grid instead")

    grid, best_value = dp_knapsack(items, capacity)
    print_grid(grid)
    print("Best value (DP, all 20 items):")
    print(best_value)

    rows = len(items) + 1
    cols = capacity + 1
    cell_count = rows * cols

    print()
    print("Naive call count (18 items):")
    print(last_naive_count)
    print("DP grid cells filled (20 items):")
    print(cell_count)
    print("The naive recursion redoes the same subproblems over and over;")
    print("the DP grid writes each subproblem's answer down exactly once.")

    print()
    print("Part 3: Point the same technique somewhere else")

    a = "hish"
    b1 = "fish"
    b2 = "vista"

    substring_fish = longest_common_substring(a, b1)
    subsequence_fish = longest_common_subsequence(a, b1)
    print("hish vs fish")
    print("longest common substring:")
    print(substring_fish)
    print("longest common subsequence:")
    print(subsequence_fish)

    substring_vista = longest_common_substring(a, b2)
    subsequence_vista = longest_common_subsequence(a, b2)
    print("hish vs vista")
    print("longest common substring:")
    print(substring_vista)
    print("longest common subsequence:")
    print(subsequence_vista)

    print()
    print("Why substring and subsequence can disagree:")
    print("Longest common substring requires the matching letters to be")
    print("consecutive in both strings, while longest common subsequence")
    print("only requires the letters to appear in the same relative order,")
    print("with gaps allowed. Two strings can share a long subsequence made")
    print("of scattered letters without ever sharing a long unbroken run,")
    print("which is exactly what happens with 'hish' and 'vista'.")

    print()
    print("Reflection: for the grid technique to work at all, a problem")
    print("must break into independent subproblems -- the answer to a")
    print("smaller piece cannot depend on choices made in a different,")
    print("unrelated piece. Other places this same idea shows up: spell")
    print("check suggestions, git diff, and DNA sequence alignment.")
