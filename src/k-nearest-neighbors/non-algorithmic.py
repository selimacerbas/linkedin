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

from sklearn.neighbors import KNeighborsClassifier

# Training Data
X = [[2, 4], [4, 2], [4, 4], [6, 6], [8, 8]]
y = ['on-time', 'on-time', 'on-time', 'late', 'late']

# Create model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predict for new package
new_package = [[5, 3]]
prediction = knn.predict(new_package)
print("Prediction:", prediction[0])
