"""
preprocessing.py
-----------------
Creates a synthetic hospital dataset and performs basic preprocessing.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 1. Generate synthetic hospital data -----------------------
np.random.seed(42)
n = 500
df = pd.DataFrame({
    "age": np.random.randint(20, 90, n),
    "num_previous_visits": np.random.randint(0, 10, n),
    "avg_stay_days": np.random.uniform(1, 15, n).round(1),
    "diagnosis": np.random.choice(["diabetes", "hypertension", "asthma", "infection"], n),
    "readmitted_30days": np.random.choice([0, 1], n, p=[0.7, 0.3])  # target variable
})

# 2. Handle categorical data --------------------------------
# Convert text (diagnosis) into numerical values using one-hot encoding
df = pd.get_dummies(df, columns=["diagnosis"], drop_first=True)

# 3. Split data for training/testing ------------------------
X = df.drop("readmitted_30days", axis=1)
y = df["readmitted_30days"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Save datasets ------------------------------------------
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("✅ Data preprocessing complete. Files saved.")
