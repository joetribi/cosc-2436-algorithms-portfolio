"""
Lab: "You Are Your Neighbors" -- Classification, Regression, and KNN

This lab builds a hand-rolled K-Nearest-Neighbors pipeline in three parts:

Part 1: Turn real things into numbers (features) and measure the
straight-line distance between them.
Part 2: Watch KNN break in two different ways -- a badly chosen k,
and features measured on wildly different scales.
Part 3: Reuse the exact same k\_nearest() neighbors for two different
endings -- classify() (majority vote) and predict\_rating()
(average) -- to see that classification and regression are
one algorithm with two different endings.

Scope: no scikit-learn, no train/test split, no accuracy metrics.
Everything below is hardcoded and deterministic -- no randomness, no
file I/O -- so results can be checked exactly.
"""

import math

# ---------------------------------------------------------------------------

# PART 1: Features and distance

# ---------------------------------------------------------------------------
# The book's oranges-vs-grapefruit dataset.
# size = diameter in cm, redness = rating from 1 (very orange) to 10 (very red)

FRUITS = [
{"size": 5, "redness": 2, "label": "orange"},
{"size": 6, "redness": 3, "label": "orange"},
{"size": 5, "redness": 1, "label": "orange"},
{"size": 6, "redness": 4, "label": "orange"},
{"size": 7, "redness": 3, "label": "orange"},
{"size": 6, "redness": 2, "label": "orange"},
{"size": 9, "redness": 6, "label": "grapefruit"},
{"size": 10, "redness": 7, "label": "grapefruit"},
{"size": 9, "redness": 8, "label": "grapefruit"},
{"size": 11, "redness": 6, "label": "grapefruit"},
{"size": 10, "redness": 9, "label": "grapefruit"},
{"size": 9, "redness": 7, "label": "grapefruit"},
]

# A fruit of unknown type -- this is what we want to classify.

NEW_FRUIT = {"size": 7, "redness": 5}

def extract_features(item):
    """
    Turn a fruit dict like {"size": 5, "redness": 2, "label": "orange"}
    into a plain list of numbers: [size, redness].

    This is the whole point of the chapter: a fruit becomes a point on
    a graph the moment you pull its numbers out.

    TODO:
      1. Read item["size"] and item["redness"].
      2. Return them as a list: [size, redness].
    """
    # TODO: implement feature extraction

    size = item["size"]
    redness = item["redness"]
    return [size, redness]


def euclidean_distance(a, b):
    """
    Compute the straight-line distance between two feature lists a and b.
    Write this out yourself with a loop -- do not import a distance
    function. It is just the Pythagorean theorem generalized to more
    than two dimensions.

    TODO:
      1. For each pair of matching values (a[i], b[i]), compute the
         squared difference (a[i] - b[i]) ** 2.
      2. Add up all the squared differences.
      3. Return the square root of that sum (math.sqrt).
    """
    # TODO: implement Euclidean distance
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2
    return math.sqrt(total)


def k_nearest(training_set, new_item, k):
    """
    Return the k training items closest to new_item, sorted from
    nearest to farthest.

    training_set: a list of dicts, each with a "features" key
                   (a list of numbers) and a "label" or "value" key.
    new_item:      a dict with a "features" key (the point we are
                   asking about).
    k:             how many neighbors to return.

    TODO:
      1. Sort training_set by distance to new_item["features"]. Use
         sorted(training_set, key=...) -- a callback to the Chapter 2
         selection sort lab. In a comment, explain what your key
         function computes for each item.
      2. Return only the first k items of that sorted list.
    """
    # TODO: implement k-nearest-neighbor lookup
    sorted_items = sorted(
        training_set,
        key=lambda item: sum(
            (a - b) ** 2
            for a, b in zip(item["features"], new_item["features"])
        )
    )

    return sorted_items[:k]


# ---------------------------------------------------------------------------
# Core KNN endings, used in Parts 1, 2, and 3
# ---------------------------------------------------------------------------

def classify(neighbors):
    """
    Majority vote: given a list of neighbor dicts (each with a "label"
    key), return the most common label.

    TODO:
      1. Count how many times each label appears among neighbors.
      2. Return the label with the highest count.
    """
    # TODO: implement majority-vote classification
    counts = {}
    for neighbor in neighbors:
        label = neighbor["label"]
        counts[label] = counts.get(label, 0) + 1

    return max(counts, key=counts.get)


def predict_rating(neighbors):
    """
    Average: given a list of neighbor dicts (each with a "value" key),
    return the average of their values.

    TODO:
      1. Add up the "value" field of every neighbor.
      2. Divide by the number of neighbors and return that average.
    """
    # Step 1: sum up every neighbor's numeric value.
    total = 0
    for neighbor in neighbors:
        total += neighbor["value"]
    # Step 2: divide by how many neighbors there are.
    return total / len(neighbors)


# ---------------------------------------------------------------------------
# PART 2: The two ways KNN goes wrong
# ---------------------------------------------------------------------------

# --- Failure A: the wrong k ------------------------------------------------
# 7 real "cat" points cluster near (1-3, 1-3). 7 real "dog" points cluster
# near (8-10, 8-10). One mislabeled "dog" outlier sits right next to the
# test point, inside the cat cluster.

TRAINING_SET_A = [
{"features": [1, 1], "label": "cat"},
{"features": [1, 2], "label": "cat"},
{"features": [2, 1], "label": "cat"},
{"features": [1, 3], "label": "cat"},
{"features": [3, 1], "label": "cat"},
{"features": [2, 3], "label": "cat"},
{"features": [3, 2], "label": "cat"},
{"features": [2, 2], "label": "dog"},  # mislabeled outlier, right next to the test point!
{"features": [8, 8], "label": "dog"},
{"features": [9, 9], "label": "dog"},
{"features": [8, 9], "label": "dog"},
{"features": [9, 8], "label": "dog"},
{"features": [10, 10], "label": "dog"},
{"features": [8, 10], "label": "dog"},
{"features": [10, 8], "label": "dog"},
]

TEST_POINT_A = {"features": [2, 2]}

# --- Failure B: unscaled features ------------------------------------------
# feature 0 = weight in grams (hundreds), feature 1 = quality rating (1-5).
# The gram-scale feature can drown out the quality feature entirely unless
# both are rescaled to the same 0-1 range.
RAW_DATASET_B = [
{"features": [500, 5], "label": "premium"},
{"features": [520, 4], "label": "premium"},
{"features": [480, 5], "label": "premium"},
{"features": [510, 4], "label": "premium"},
{"features": [495, 5], "label": "premium"},
{"features": [505, 4], "label": "premium"},
{"features": [150, 1], "label": "standard"},
{"features": [160, 2], "label": "standard"},
{"features": [140, 1], "label": "standard"},
{"features": [155, 2], "label": "standard"},
{"features": [145, 1], "label": "standard"},
{"features": [165, 2], "label": "standard"},
]

TEST_POINT_B = {"features": [300, 5]}

def normalize(dataset):
    """
    Rescale every feature in dataset to a 0-1 range, using min-max
    normalization: (value - min) / (max - min) for each feature column.

    dataset: a list of dicts, each with a "features" key.
    Returns a NEW list of dicts (same other keys, rescaled features).
    """
    num_features = len(dataset[0]["features"])

    # Step 1: find the min and max of each feature column.
    mins = []
    maxs = []
    for i in range(num_features):
        column_values = [item["features"][i] for item in dataset]
        mins.append(min(column_values))
        maxs.append(max(column_values))

    # Step 2: rebuild every item with rescaled features.
    normalized = []
    for item in dataset:
        new_features = []
        for i in range(num_features):
            value = item["features"][i]
            min_val = mins[i]
            max_val = maxs[i]
            if max_val == min_val:
                scaled = 0.0
            else:
                scaled = (value - min_val) / (max_val - min_val)
            new_features.append(scaled)
        new_item = dict(item)  # copy so we don't mutate the original
        new_item["features"] = new_features
        normalized.append(new_item)

    return normalized

# ---------------------------------------------------------------------------
# PART 3: Same neighbors, different question -- regression
# ---------------------------------------------------------------------------

# Each user rated 3 movies everyone has seen ("features"), plus the movie
# we want to predict ("value" = star rating 1-5). "label" is just a
# derived like/dislike bucket from that same rating, so the SAME neighbor
# list can be used for both classify() and predict_rating().
USERS = [
{"name": "Alice", "features": [5, 2, 1], "value": 5, "label": "likes"},
{"name": "Bob", "features": [4, 3, 2], "value": 4, "label": "likes"},
{"name": "Carol", "features": [5, 1, 1], "value": 5, "label": "likes"},
{"name": "Dave", "features": [2, 4, 5], "value": 2, "label": "dislikes"},
{"name": "Eve", "features": [1, 5, 4], "value": 1, "label": "dislikes"},
{"name": "Frank", "features": [3, 3, 3], "value": 3, "label": "dislikes"},
{"name": "Grace", "features": [5, 2, 2], "value": 4, "label": "likes"},
{"name": "Heidi", "features": [2, 5, 5], "value": 2, "label": "dislikes"},
{"name": "Ivan", "features": [4, 2, 1], "value": 5, "label": "likes"},
{"name": "Judy", "features": [1, 4, 5], "value": 1, "label": "dislikes"},
]

# Sam has rated the same 3 movies but has NOT seen the target movie yet.

TARGET_USER = {"name": "Sam", "features": [5, 2, 1]}

def recommend(user, users, k):
    """
    Given a target user and a table of other users, predict how the
    target user would rate the one movie they haven't rated yet, based
    on the k most similar users (measured by their ratings on the
    movies the target user HAS rated).

    Returns a tuple: (movie_title, predicted_rating).
    """
    neighbors = k_nearest(users, user, k)
    predicted_rating = predict_rating(neighbors)
    return predicted_rating


# ---------------------------------------------------------------------------
# Main program -- runs all three parts with hardcoded, deterministic data
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("PART 1: Features and distance")
    print("=" * 70)

    # Turn every fruit dict into a {"features": [...], "label": ...} record.
    training_fruits = [
        {"features": extract_features(fruit), "label": fruit["label"]}
        for fruit in FRUITS
    ]
    new_fruit_features = extract_features(NEW_FRUIT)
    print("New fruit features (size, redness):", new_fruit_features)

    sample = training_fruits[0]
    dist = euclidean_distance(sample["features"], new_fruit_features)
    print(f"Distance from new fruit to first training fruit {sample['features']}: {dist:.2f}")

    neighbors = k_nearest(training_fruits, {"features": new_fruit_features}, 3)
    print("3 nearest neighbors to the new fruit:")
    for n in neighbors:
        print(f"  features={n['features']} label={n['label']}")

    prediction = classify(neighbors)
    print(f"Predicted label for new fruit: {prediction}")

    print()
    print("=" * 70)
    print("PART 2a: Failure mode -- the wrong k")
    print("=" * 70)
    for k in [1, 3, 15]:
        neighbors_a = k_nearest(TRAINING_SET_A, TEST_POINT_A, k)
        prediction_a = classify(neighbors_a)
        print(f"k={k:2d} -> predicted label: {prediction_a}")

    print("Explanation:")
    print("  At k=1, the single nearest neighbor is the mislabeled 'dog'")
    print("  outlier sitting right on top of the test point, so a tiny")
    print("  labeling mistake in the data completely controls the answer.")
    print("  At k=15, EVERY training point is included, so locality no")
    print("  longer matters at all -- the prediction just becomes whichever")
    print("  class happens to have more members overall (dog, 8 vs 7),")
    print("  even though the test point sits inside the cat cluster.")

    print()
    print("=" * 70)
    print("PART 2b: Failure mode -- unscaled features")
    print("=" * 70)

    print("Raw features (weight in grams, quality rating 1-5):")
    neighbors_b_raw = k_nearest(RAW_DATASET_B, TEST_POINT_B, 3)
    prediction_b_raw = classify(neighbors_b_raw)
    print(f"  Prediction using raw features: {prediction_b_raw}")

    # Normalize the training set and the test point TOGETHER, so they
    # are rescaled using the exact same min/max for each feature column.
    combined = RAW_DATASET_B + [{"features": TEST_POINT_B["features"]}]
    combined_normalized = normalize(combined)
    training_b_normalized = combined_normalized[:-1]
    test_point_b_normalized = combined_normalized[-1]

    print("Normalized features (0-1 scale):")
    neighbors_b_norm = k_nearest(training_b_normalized, test_point_b_normalized, 3)
    prediction_b_norm = classify(neighbors_b_norm)
    print(f"  Prediction using normalized features: {prediction_b_norm}")

    print("Explanation:")
    print("  With raw features, the weight-in-grams values (hundreds) are")
    print("  so much larger than the 1-5 quality scores that distance is")
    print("  decided almost entirely by weight -- the quality feature is")
    print("  effectively drowned out because grams and stars are not the")
    print("  same units. Once every feature is rescaled to 0-1, both")
    print("  features contribute fairly, and the prediction changes.")

    print()
    print("=" * 70)
    print("PART 3: Same neighbors, different question -- regression")
    print("=" * 70)

    # Build a demo dataset where every fruit has BOTH a "label" (for
    # classification) and a "value" (for regression) -- here we reuse
    # redness as a stand-in numeric target to predict.
    demo_training = [
        {
            "features": extract_features(fruit),
            "label": fruit["label"],
            "value": fruit["redness"],
        }
        for fruit in FRUITS
    ]
    demo_neighbors = k_nearest(demo_training, {"features": new_fruit_features}, 3)

    # Same neighbors, two different endings -- the ONLY thing that changes
    # below is what we do with demo_neighbors once we have it: classify()
    # takes a majority vote, predict_rating() takes an average.
    demo_label = classify(demo_neighbors)
    demo_value = predict_rating(demo_neighbors)
    print("Classification and regression from the SAME k_nearest() call:")
    print(f"  classify(neighbors)       -> {demo_label}")
    print(f"  predict_rating(neighbors) -> {demo_value:.2f}")

    predicted_rating = recommend(TARGET_USER, USERS, 3)
    print(f"Predicted rating for {TARGET_USER['name']}: {predicted_rating:.2f}")

    print()
    print("=" * 70)
    print("Reflection")
    print("=" * 70)
    print("To recommend restaurants, useful features might be: average")
    print("price, cuisine type (encoded as a number), distance from home,")
    print("and average star rating. If one of those features were the")
    print("same value for every restaurant in the dataset (e.g. every")
    print("restaurant is in the same city), that feature would add zero")
    print("information -- it could never help distinguish one restaurant")
    print("from another, since its distance contribution would always be")
    print("the same for every comparison.")


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# REFLECTION (answer in comments below, no code needed):
#
# 1. If you were building a KNN recommender for restaurants, what features would you extract from each restaurant?
#    If I were building a KNN recommender for restaurants, I would use features such as price range, customer rating, distance from the user, cuisine type represented numerically, average wait time, and the restaurant's atmosphere or noise level.

# 2. What would go wrong if one of those features had the exact same value for every restaurant in your dataset?
#   If one feature had the exact same value for every restaurant, it would not help distinguish between restaurants. Its value would have no effect on which restaurants are considered nearest, so it would essentially be useless for KNN.
# ---------------------------------------------------------------------------
