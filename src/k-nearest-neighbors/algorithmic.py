# Challenge Question
#
# You run a mini-delivery startup. Based on past delivery success, you want to predict whether a new package will be delivered on time based on:
# Distance (in km)
# Weight (in kg)
# You have some past data. Can you use KNN to predict the outcome?

# Hints:
#
# Normalize your data!
# Try with k=3 and play around with other values.
# Use Euclidean distance for simplicity.

import math
from collections import Counter

# Training data
data = [
    ([2, 4], 'on-time'),
    ([4, 2], 'on-time'),
    ([4, 4], 'on-time'),
    ([6, 6], 'late'),
    ([8, 8], 'late')
]

# New point
target = [5, 3]

# Euclidean Distance function
def euclidean(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# Compute distances
distances = [(euclidean(target, point), label) for point, label in data]

# Sort and pick k nearest
k = 3
nearest = sorted(distances)[:k]
labels = [label for _, label in nearest]

# Predict by majority vote
prediction = Counter(labels).most_common(1)[0][0]
print("Prediction:", prediction)

