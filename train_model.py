"""
train_model.py
---------------
Trains a logistic regression model on the hospital dataset and evaluates it.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
import joblib

# 1. Load preprocessed data -------------------------------
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv").values.ravel()
y_test = pd.read_csv("y_test.csv").values.ravel()

# 2. Initialize the model ----------------------------------
model = LogisticRegression(max_iter=1000)

# 3. Train the model ---------------------------------------
model.fit(X_train, y_train)

# 4. Evaluate model ----------------------------------------
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# 5. Save trained model ------------------------------------
joblib.dump(model, "readmission_model.pkl")
print("✅ Model trained and saved as readmission_model.pkl")
