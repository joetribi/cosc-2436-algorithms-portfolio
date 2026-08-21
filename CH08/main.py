"""
Lab: "Out of Balance" -- Binary Search Trees and Why Shape Matters

Part 1: Build a working BST (insert, search, height, in_order)
Part 2: Watch a BST degenerate into a linked list on sorted input
Part 3: Rotate to fix it (single rotations you implement, double
        rotations provided pre-written, then avl_insert)

Determinism note: every value in this file is hardcoded. No randomness,
no file I/O -- so results (heights, comparison counts) are always the
same every time you run this file.
"""


class BSTNode:
    """A single node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------------------------------------------------------------------
# PART 1: Build a working BST
# ---------------------------------------------------------------------------

def insert(root, value):
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def search(root, value):
    comparisons = 0
    node = root

    while node is not None:
        comparisons += 1
        if node.value == value:
            return (True, comparisons)
        elif value < node.value:
            node = node.left
        else:
            node = node.right

    return (False, comparisons)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def in_order(root, result=None):
    if result is None:
        result = []

    if root is None:
        return result

    in_order(root.left, result)
    result.append(root.value)
    in_order(root.right, result)

    return result

# ---------------------------------------------------------------------------
# PART 2: Watch it degenerate (constructed counterexample)
# ---------------------------------------------------------------------------


def compare_bst_shapes():
    mixed_order = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65]
    sorted_order = sorted(mixed_order)
    largest_value = max(mixed_order)

    tree_a = None
    tree_b = None

    for value in mixed_order:
        tree_a = insert(tree_a, value)

    for value in sorted_order:
        tree_b = insert(tree_b, value)

    height_a = height(tree_a)
    height_b = height(tree_b)
    in_order_a = in_order(tree_a)
    in_order_b = in_order(tree_b)
    found_a, comparisons_a = search(tree_a, largest_value)
    found_b, comparisons_b = search(tree_b, largest_value)

    print("Tree A height:", height_a)
    print("Tree B height:", height_b)
    print("Tree A in-order:", in_order_a)
    print("Tree B in-order:", in_order_b)
    print("Tree A search comparisons for largest value:", comparisons_a)
    print("Tree B search comparisons for largest value:", comparisons_b)

    
    return tree_a, tree_b

#---------------------------------------------------------------------------
# PART 3: Rotate to fix it
# ---------------------------------------------------------------------------

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def rotate_right(node):
    pivot = node.left
    node.left = pivot.right
    pivot.right = node
    return pivot


def rotate_left(node):
    pivot = node.right
    node.right = pivot.left
    pivot.left = node
    return pivot # placeholder


def rotate_left_right(node):
    """Double rotation for the LR case (provided, no need to modify)."""
    node.left = rotate_left(node.left)
    return rotate_right(node)


def rotate_right_left(node):
    """Double rotation for the RL case (provided, no need to modify)."""
    node.right = rotate_right(node.right)
    return rotate_left(node)


def avl_insert(root, value):
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = avl_insert(root.left, value)
    else:
        root.right = avl_insert(root.right, value)

    balance = balance_factor(root)

    if balance > 1 and value < root.left.value:
        return rotate_right(root)
    if balance < -1 and value >= root.right.value:
        return rotate_left(root)
    if balance > 1 and value >= root.left.value:
        return rotate_left_right(root)
    if balance < -1 and value < root.right.value:
        return rotate_right_left(root)

    return root # placeholder


if __name__ == "__main__":
    print("=== Part 2: Watch it degenerate ===")
    tree_a, tree_b = compare_bst_shapes()

    print()
    print("=== Part 3: Rotate to fix it ===")
    mixed_order = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65]
    sorted_order = sorted(mixed_order)

    avl_root = None
    for value in sorted_order:
        avl_root = avl_insert(avl_root, value)

    print("AVL height after sorted insertion:", height(avl_root))
    print("AVL in-order:", in_order(avl_root))
