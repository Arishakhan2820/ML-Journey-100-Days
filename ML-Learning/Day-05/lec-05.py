# ==========================================
# Day 05: Online Learning vs Offline Learning
# ==========================================

import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor

print("==========================================")
print(" 1. BATCH (OFFLINE) LEARNING EXAMPLE")
print("==========================================")

# Full dataset loaded all at once into memory
X_batch = np.array([[500], [800], [1200], [1500]])
y_batch = np.array([50, 80, 120, 150])

# Train model once using fit() on the full data batch
batch_model = LinearRegression()
batch_model.fit(X_batch, y_batch)
print("-> Batch model trained on full dataset at once successfully!\n")


print("==========================================")
print(" 2. ONLINE (INCREMENTAL) LEARNING EXAMPLE")
print("==========================================")

# Initialize online model that supports incremental updates
online_model = SGDRegressor()

# Simulate live stream chunk 1 arriving in production
X_stream_1 = np.array([[500]])
y_stream_1 = np.array([50])
online_model.partial_fit(X_stream_1, y_stream_1)
print("-> Trained on live data chunk 1!")

# Simulate live stream chunk 2 arriving later (learned incrementally without resetting past knowledge)
X_stream_2 = np.array([[800], [1200]])
y_stream_2 = np.array([80, 120])
online_model.partial_fit(X_stream_2, y_stream_2)
print("-> Trained on live data chunk 2 on the fly!")

# Make a live prediction using the updated online model
test_house = np.array([[1000]])
predicted_price = online_model.predict(test_house)
print(f"\n-> Live Prediction for 1000 sq ft house: ${predicted_price[0]:.2f}k")
