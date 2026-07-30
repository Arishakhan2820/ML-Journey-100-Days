# 5. Python Code Example: Simulating Batch Learning Training
# To understand how a batch learning model is trained on a complete dataset in Python using Scikit-Learn, look at the code below.

# This example uses a simple Linear Regression model trained all at once on a batch of house size data to predict house prices.

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare the Complete Batch Data (Inputs: House Size in sq ft)
# X represents our features (Batch of data)
X_batch = np.array([[500], [800], [1200], [1500], [2000]])

# y represents our target labels (Prices in thousands)
y_batch = np.array([50, 80, 120, 150, 200])

print("Total training samples in batch:", len(X_batch))

# 2. Initialize the Model
model = LinearRegression()

# 3. Train the model using the ENTIRE batch at once (Batch Learning approach)
model.fit(X_batch, y_batch)
print("Model training completed on the full batch!")

# 4. Use the trained model in production/inference for new queries
new_houses = np.array([[1000], [1700]])
predictions = model.predict(new_houses)

print("\nPredictions for new batch data:")
for house_size, pred_price in zip(new_houses, predictions):
    print(f"House Size: {house_size[0]} sq ft --> Predicted Price: ${pred_price:.2f}k")

# Code Explanation:
# X_batch & y_batch: We feed the entire block of data simultaneously. No incremental splitting or streaming is used here.

# model.fit(): This function executes the batch training process over the complete dataset.

# model.predict(): Once trained offline, the static model uses these learned weights to serve real-time user requests.
