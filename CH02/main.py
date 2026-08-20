
# Lab Exercise: Selection Sort
# Course: Introduction to Algorithms
# Reference: Grokking Algorithms, Chapter 2 -- Selection Sort

# Complete the TODOs below to implement:
#  1. find_smallest(arr)
#  2. selection_sort(arr)
#  3. rank_artists(plays)



def find_smallest(arr):
    """
    Return the INDEX of the smallest element in arr.
    """
    smallest_value = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    """
    Return a NEW list containing the elements of arr sorted from
    smallest to largest. The original list must NOT be modified.
    """
    arr_copy = arr[:]
    result = []

    while arr_copy:
        smallest_index = find_smallest(arr_copy)
        smallest_value = arr_copy.pop(smallest_index)
        result.append(smallest_value)

    return result


def rank_artists(plays):
    """
    plays: a dict mapping artist name -> play count

    Return a list of artist names ordered from MOST played to
    LEAST played.
    """
    artist_counts = list(plays.items())
    remaining = artist_counts[:]
    result = []

    while remaining:
        largest_index = 0
        largest_count = remaining[0][1]

        for i in range(1, len(remaining)):
            if remaining[i][1] > largest_count:
                largest_count = remaining[i][1]
                largest_index = i

        largest_pair = remaining.pop(largest_index)
        result.append(largest_pair[0])

    return result


if __name__ == "__main__":
    # ---- Part 1 tests: find_smallest ----
    print(find_smallest([5, 3, 6, 2, 10]))   # expected: 3
    print(find_smallest([1, 2, 3]))          # expected: 0
    print(find_smallest([7]))                # expected: 0

    # ---- Part 2 tests: selection_sort ----
    print(selection_sort([5, 3, 6, 2, 10]))  # expected: [2, 3, 5, 6, 10]
    print(selection_sort([]))                # expected: []
    print(selection_sort([4, 4, 1]))         # expected: [1, 4, 4]

    original = [9, 1, 5]
    selection_sort(original)
    print(original)                          # expected: [9, 1, 5] (unchanged!)

    # ---- Part 3 test: rank_artists ----
    plays = {
        "Radiohead": 156,
        "Kishore Kumar": 141,
        "The Black Keys": 35,
        "Neutral Milk Hotel": 94,
        "Beck": 88,
        "The Strokes": 61,
        "Wilco": 111,
    }
    print(rank_artists(plays))
    # expected: ['Radiohead', 'Kishore Kumar', 'Wilco', 'Neutral Milk Hotel',
    #            'Beck', 'The Strokes', 'The Black Keys']

# ---- Part 4: Analysis Questions ----
# 1. The overall running time of selection sort is (O(n^2)). This is because the find_smallest function, which runs in (O(n)), is called (n) times (once for each element in the list). So, if you multiply the two, you get: [ O(n) \times O(n) = O(n^2) ]

# 2. Even though each pass checks about ( \frac{1}{2}n ) elements on average, the big-O notation expresses the upper bound of the running time. The (O(n^2)) notation captures the worst-case scenario where every element must be compared to find the smallest. When analyzing algorithms, we focus on the dominant factor, which, in this case, remains (n^2), as the constant factors (like ( \frac{1}{2} )) are ignored in big-O notation.

# 3. The pop() method on a list in Python has a time complexity of (O(n)) when removing an element from the middle of the list. This is because all subsequent elements must be shifted one position to fill the gap. However, the overall big-O of selection sort remains (O(n^2)) because the dominant factor in the algorithm is still the number of calls to find_smallest (each taking (O(n))). Although the pop() operation adds a cost, the total operations still fall within the (O(n^2)) bound when combined with the number of times find_smallest is called.

# ---- Challenge (Optional): in-place selection sort ----
def selection_sort_in_place(arr):
    """
    Sorts arr in place (modifies the original list) by repeatedly
    finding the smallest remaining element and swapping it into
    its correct position.
    """
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# Advantage of in-place sorting: it uses O(1) extra space (aside from a
# few index variables), since it never builds a second list.
