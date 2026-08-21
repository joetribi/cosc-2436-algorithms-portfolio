"""
File System Explorer - Recursive Directory Search
COSC 2436 - Chapter 3: Recursion
"""


# ---------------------------------------------------------------------------
# Provided helper functions (already implemented)
# ---------------------------------------------------------------------------

def trace_enter(label, depth):
    indent = "  " * depth
    print(indent + "-> entering: " + str(label))


def trace_exit(label, depth):
    indent = "  " * depth
    print(indent + "<- exiting: " + str(label))


# ---------------------------------------------------------------------------
# Task 1: find_file(structure, target_name)
# ---------------------------------------------------------------------------

def find_file(structure, target_name, current_path="", depth=0):
    new_path = current_path + "/" + structure["name"]
    trace_enter(new_path, depth)

    # BASE CASE #1: a plain file
    if structure["type"] == "file":
        if structure["name"] == target_name:
            trace_exit(new_path + " (FOUND!)", depth)
            return new_path
        trace_exit(new_path, depth)
        return None

    # RECURSIVE CASE: a folder with contents to search
    if structure["type"] == "folder":
        for item in structure["contents"]:
            result = find_file(item, target_name, new_path, depth + 1)
            if result is not None:
                trace_exit(new_path, depth)
                return result

        # BASE CASE #2: searched every item, nothing matched
        trace_exit(new_path, depth)
        return None

    trace_exit(new_path, depth)
    return None


# ---------------------------------------------------------------------------
# Task 2: count_files(structure)
# ---------------------------------------------------------------------------

def count_files(structure, depth=0):
    trace_enter(structure["name"], depth)

    # BASE CASE: a plain file always counts as exactly one file
    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return 1

    # RECURSIVE CASE: sum the counts of everything inside the folder
    if structure["type"] == "folder":
        total = 0
        for item in structure["contents"]:
            total += count_files(item, depth + 1)
        trace_exit(structure["name"], depth)
        return total

    trace_exit(structure["name"], depth)
    return 0


# ---------------------------------------------------------------------------
# Task 3: total_size(structure)
# ---------------------------------------------------------------------------

def total_size(structure, depth=0):
    trace_enter(structure["name"], depth)

    # BASE CASE: a plain file contributes its own size
    if structure["type"] == "file":
        trace_exit(structure["name"], depth)
        return structure["size"]

    # RECURSIVE CASE: accumulate the sizes of everything inside
    if structure["type"] == "folder":
        running_total = 0
        for item in structure["contents"]:
            running_total += total_size(item, depth + 1)
        trace_exit(structure["name"], depth)
        return running_total

    trace_exit(structure["name"], depth)
    return 0


# ---------------------------------------------------------------------------
# Task 4 (Stretch/Bonus): print_tree_with_depth(structure, depth=0)
# ---------------------------------------------------------------------------

def print_tree_with_depth(structure, depth=0):
    print("  " * depth + structure["name"])

    # BASE CASE: a file has no children to recurse into
    if structure["type"] == "file":
        return

    # RECURSIVE CASE: print each child one level deeper
    if structure["type"] == "folder":
        for item in structure["contents"]:
            print_tree_with_depth(item, depth + 1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sample_structure = {
        "name": "root",
        "type": "folder",
        "contents": [
            {"name": "readme.txt", "type": "file", "size": 120},
            {
                "name": "docs",
                "type": "folder",
                "contents": [
                    {"name": "notes.txt", "type": "file", "size": 200},
                    {
                        "name": "archive",
                        "type": "folder",
                        "contents": [
                            {"name": "old.txt", "type": "file", "size": 50},
                        ],
                    },
                ],
            },
            {"name": "empty_folder", "type": "folder", "contents": []},
        ],
    }

    print("=== Searching for notes.txt ===")
    found_path = find_file(sample_structure, "notes.txt")
    print("Result:", found_path)

    print("\n=== Searching for missing.txt ===")
    missing_path = find_file(sample_structure, "missing.txt")
    print("Result:", missing_path)

    print("\n=== Counting files ===")
    print("Total files:", count_files(sample_structure))

    print("\n=== Total size ===")
    print("Total size:", total_size(sample_structure))

    print("\n=== Tree view ===")
    print_tree_with_depth(sample_structure)
