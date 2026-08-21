# Lab Report — Chapter 12: K-Nearest Neighbors

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — the k comparison, the before/after normalization results, and your recommendation.*

```text

```

## Reflection Questions

1. **Explain k-nearest neighbors to someone who has never programmed.**
   - *"You're similar to the people around you" is the whole idea.*
      - *KNN looks at how similar items are by comparing their features. For example, if you're looking for a new restaurant, KNN checks which restaurants are most like the ones you've enjoyed before, based on features like cuisine type, price, and rating. The idea is that if you liked certain places, you'll likely enjoy similar ones.*

2. **Two classmates pick k = 1 and k = 15 on the same data and get different answers. What is each one doing wrong, or right?**
   - *k = 1: This approach may lead to overfitting. The student is relying on just the nearest neighbor, which might not represent the overall trend of the data. A single outlier could skew the recommendation.*
   - *k = 15: This choice might provide a more generalized view, but if the dataset is small, it can include too many irrelevant neighbors, leading to dilution of the true signal. The student might end up averaging out important distinctions. Both students have valid approaches, but they need to consider the context and nature of their data to choose an appropriate k.*

3. **Chapter 12 says Netflix-style recommendations work this way. Describe how someone's viewing history becomes the "features."**
   - *A person's viewing history becomes their features. For example, the movies they watched, rated, or liked can be represented as numbers. KNN compares these features with other users to find people with similar viewing habits. Then it can recommend movies that those similar users enjoyed.*
