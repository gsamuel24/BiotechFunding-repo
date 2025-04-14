import pandas as pd
from sklearn.model_selection import train_test_split

# Custom preprocessing functions
from utils import collapse_categories, count_encode, encode_data, model_impute_missing_values

# Load cleaned dataset
df = pd.read_csv("updated_dataframe.csv")

# Define target and feature set
X = df.drop(columns=["amount"])
y = df["amount"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Encode categorical variables
X_train_encoded, X_test_encoded = encode_data(X_train, X_test)

# Handle missing values, transformations, modeling, etc.
# (Add additional steps here or call functions from utils)

print("Data loaded and encoded successfully.")
