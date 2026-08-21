"""
Lab: Six Degrees -- Graph Modeling & Breadth-First Search
Chapter 6 concepts: representing a network as a graph (dict of lists),
and using a queue-based BFS to answer "is there a path?" and
"what's the shortest path?", plus a topological sort mini-exercise.

Fill in the TODO sections. Do not change the shape of the data
structures or the function signatures.
"""

from collections import deque


# ---------------------------------------------------------------------------
# PART 1 DATA: a small professional/social network
# graph["you"] = ["alice", "bob", "claire"]  <-- book's exact pattern
# NOTE: this graph deliberately contains a CYCLE (peggy -> you) so that
# your search() function MUST use a `searched` set or it will hang forever!
# ---------------------------------------------------------------------------
network = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "peggy": ["you", "maria"],   # cycle back to "you"!
    "anuj": [],
    "thom": ["diego"],
    "jonny": ["sam"],
    "maria": ["lee"],
    "diego": [],
    "sam": [],
    "lee": [],
}

# Which skill(s) each person has. Used by person_has_skill().
skills = {
    "you": ["project_management"],
    "alice": ["design"],
    "bob": ["sales"],
    "claire": ["marketing"],
    "peggy": ["finance"],
    "anuj": ["manufacturing"],
    "thom": ["design"],
    "jonny": ["sales"],
    "maria": ["manufacturing"],
    "diego": ["python"],
    "sam": ["python"],
    "lee": ["manufacturing"],
}


def person_has_skill(name, skill_to_find):
    persons_skills = skills.get(name, [])
    return skill_to_find in persons_skills


def search(start_name, skill_to_find):
    search_queue = deque()
    search_queue.extend(network[start_name])
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_has_skill(person, skill_to_find):
                return True
            else:
                search_queue.extend(network[person])
                searched.add(person)
    return False


# ---------------------------------------------------------------------------
# PART 2: shortest path (degree of separation), not just True/False
# ---------------------------------------------------------------------------
def search_shortest_path(start_name, skill_to_find):
    search_queue = deque([(neighbor, 1) for neighbor in network[start_name]])
    searched = set()

    while search_queue:
        person, distance = search_queue.popleft()
        if person not in searched:
            if person_has_skill(person, skill_to_find):
                return distance
            else:
                for neighbor in network[person]:
                    search_queue.append((neighbor, distance + 1))
                searched.add(person)

    return -1

def search_with_path(start_name, skill_to_find):
    # TODO: Step 1 - create search_queue with start_name's direct neighbors
    # TODO: Step 2 - create an empty `searched` set
    # TODO: Step 3 - create a `came_from` dict; for each of start_name's
    #                direct neighbors, came_from[neighbor] = start_name
    # TODO: Step 4 - loop while search_queue is not empty:
    #                 a) pop a person off the queue
    #                 b) if person not in searched:
    #                      - if they have the skill: reconstruct the path
    #                        by walking came_from backwards from person to
    #                        start_name, then reverse it and return it
    #                      - else, for each neighbor not yet in came_from,
    #                        set came_from[neighbor] = person and enqueue it
    #                      - add person to searched
    # TODO: Step 5 - return [] if nobody found
    search_queue = deque(network[start_name])
    searched = set()
    came_from = {neighbor: start_name for neighbor in network[start_name]}

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_has_skill(person, skill_to_find):
                # walk backwards through came_from to build the path
                path = [person]
                while path[-1] != start_name:
                    path.append(came_from[path[-1]])
                path.reverse()
                return path
            else:
                for neighbor in network[person]:
                    if neighbor not in came_from:
                        came_from[neighbor] = person
                        search_queue.append(neighbor)
                searched.add(person)

    return []


# ---------------------------------------------------------------------------
# PART 3: topological sort mini-exercise
# A small DAG modeling steps to set up a GitHub Classroom assignment.
# ---------------------------------------------------------------------------
# dependency_graph[step] = [steps that must happen BEFORE `step`]
dependency_graph = {
    "create_repo_template": [],
    "write_starter_code": ["create_repo_template"],
    "write_tests": ["write_starter_code"],
    "create_classroom_assignment": ["write_starter_code", "write_tests"],
    "invite_students": ["create_classroom_assignment"],
    "grade_submissions": ["invite_students"],
}

# A proposed ordering to check for validity (Exercise 6.3 style)
proposed_order = [
    "create_repo_template",
    "write_starter_code",
    "write_tests",
    "create_classroom_assignment",
    "invite_students",
    "grade_submissions",
]


def is_valid_order(order, dep_graph):
    """
    Return True if "order" is a valid topological ordering of dep_graph,
    i.e. every step appears only after all of its dependencies.
    """
    # Step 1 - map each step to its position in the order
    position = {}
    for i, step in enumerate(order):
        position[step] = i

    # Step 2 - verify every dependency comes before its step
    for step, dependencies in dep_graph.items():
        for dependency in dependencies:
            if position[dependency] > position[step]:
                return False

    # Step 3 - no violations found
    return True


def topological_sort(dep_graph):
    """
    Return a valid topological ordering (list of step names) of dep_graph.
    """
    # TODO: Step 1 - create an empty list called `order`
    order = []
    # TODO: Step 2 - loop until len(order) == len(dep_graph):
    #                 a) look through dep_graph for a step not yet in order
    #                    whose dependencies are ALL already in order
    #                 b) append that step to order
    while len(order) < len(dep_graph):
        for step, dependencies in dep_graph.items():
            if step not in order:
                # Check whether all dependencies are already in order
                if all(dep in order for dep in dependencies):
                    order.append(step)
                    break

    # TODO: Step 3 - return order
    return order


if __name__ == "__main__":
    print("Does anyone in my network know Python?",
          search("you", "python"))                     # Expect: True

    print("Does anyone know astronomy?",
          search("you", "astronomy"))                  # Expect: False

    print("Hops to nearest manufacturing contact:",
          search_shortest_path("you", "manufacturing")) # Expect: 2

    print("Hops to nearest python contact:",
          search_shortest_path("you", "python"))        # Expect: 3

    print("Hops to nonexistent skill:",
          search_shortest_path("you", "astronomy"))     # Expect: -1

    print("Path to manufacturing contact:",
          search_with_path("you", "manufacturing"))     # Expect: ['you', 'bob', 'anuj']
