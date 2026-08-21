import time

# ============================================================
# PART 1: Three Classic Hash Table (dict) Use Cases
# ============================================================

# ---- Use Case 1: Lookup Tool (Contact Book) ----

def add_contact(contact_book, name, number):
    contact_book[name] = number


def lookup_contact(contact_book, name):
    return contact_book.get(name, "Not found")


# ---- Use Case 2: Duplicate-Catcher (Voter Check) ----

def check_voter(voted_dict, name):
    if name in voted_dict:
        return "Already voted!"
    else:
        voted_dict[name] = True
        return "Allowed to vote"


# ---- Use Case 3: Cache Simulator (Web Page Cache) ----

def simulate_server_call(url):
    time.sleep(0.01)
    return "Contents of " + url


def get_page(cache, url):
    if url in cache:
        print("HIT:", url)
        return cache[url]
    else:
        print("MISS:", url)
        result = simulate_server_call(url)
        cache[url] = result
        return result


# ============================================================
# PART 2: Build Your Own Mini Hash Table
# ============================================================

def simple_hash(key, num_slots):
    total = 0
    for char in key:
        total += ord(char)
    return total % num_slots


class MiniHashTable:
    """
    A simplified hash table built on a plain Python list.
    Collisions are handled via chaining: each slot holds a list of
    (key, value) pairs.
    """

    def __init__(self, num_slots):
        self.num_slots = num_slots
        # Each slot starts as an empty list (chain) for collision resolution
        self.slots = [[] for _ in range(num_slots)]
        self.num_items = 0

    def insert(self, key, value):
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]

        for i in range(len(chain)):
            existing_key, existing_value = chain[i]
            if existing_key == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))
        self.num_items += 1

    def get(self, key):
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]

        for existing_key, existing_value in chain:
            if existing_key == key:
                return existing_value
        return None

    def load_factor(self):
        return self.num_items / self.num_slots


# ============================================================
# PART 3: Load Factor & Hash Quality Investigation
# ============================================================

def bad_hash(key, num_slots):
    return len(key) % num_slots


def investigate_hash_quality(hash_func, keys, num_slots):
    chains = [[] for _ in range(num_slots)]
    total_collisions = 0

    for key in keys:
        index = hash_func(key, num_slots)
        if len(chains[index]) >= 1:
            total_collisions += 1
        chains[index].append(key)

    longest_chain_length = 0
    for chain in chains:
        if len(chain) > longest_chain_length:
            longest_chain_length = len(chain)

    return total_collisions, longest_chain_length



# ============================================================
# MAIN PROGRAM - Deterministic demo data (no files, no randomness)
# ============================================================

if __name__ == "__main__":
    # ---- Part 1 Demo: Contact Book ----
    contact_book = {}
    add_contact(contact_book, "Alice", "555-1234")
    add_contact(contact_book, "Bob", "555-5678")
    print("Alice's number:", lookup_contact(contact_book, "Alice"))
    print("Looking up Charlie:", lookup_contact(contact_book, "Charlie"))

    # ---- Part 1 Demo: Voter Check ----
    voted_dict = {}
    voters_to_check = ["Alice", "Bob", "Alice", "Carol", "Bob", "Bob"]
    duplicate_attempts = 0
    for voter in voters_to_check:
        result = check_voter(voted_dict, voter)
        print(voter, "->", result)
        if result == "Already voted!":
            duplicate_attempts += 1
    print("Total duplicate vote attempts:", duplicate_attempts)

    # ---- Part 1 Demo: Cache Simulator ----
    cache = {}
    urls_to_fetch = ["/home", "/about", "/home", "/contact", "/about", "/home"]
    for url in urls_to_fetch:
        contents = get_page(cache, url)
        print(contents)

    # ---- Part 2 Demo: Mini Hash Table ----
    table = MiniHashTable(5)
    table.insert("apple", 1)
    table.insert("banana", 2)
    table.insert("cherry", 3)
    print("apple ->", table.get("apple"))
    print("banana ->", table.get("banana"))
    print("Load factor:", table.load_factor())

    # ---- Part 3 Demo: Hash Quality Investigation ----
    keys = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Heidi"]
    num_slots = 5

    bad_collisions, bad_longest = investigate_hash_quality(bad_hash, keys, num_slots)
    print("Bad hash -> collisions:", bad_collisions, "longest chain:", bad_longest)

    good_collisions, good_longest = investigate_hash_quality(simple_hash, keys, num_slots)
    print("Simple hash -> collisions:", good_collisions, "longest chain:", good_longest)
