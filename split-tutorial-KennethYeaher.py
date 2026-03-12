import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data 
housing = fetch_california_housing(as_frame=True)
df = housing.frame  

#feature and target
X = df.drop(columns="MedHouseVal")
y = df["MedHouseVal"]

# --- Train/test split ---
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Build + train Linear Regression model ---
model = LinearRegression()
model.fit(x_train, y_train)

# --- R^2 scores ---
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)

# --- Predictions on the test set ---
predictions = model.predict(x_test)

# --- Sample of actual vs predicted (first 10) ---
sample_predictions = pd.DataFrame(
    {"Actual": y_test.iloc[:10].values, "Predicted": predictions[:10]}
)

# --- Print output (for your screenshot submission) ---
print("\nR^2 scores:")
print("Train R^2 score:", train_score)
print("Test R^2 score:", test_score)

print("\nSample Predictions (First 10):")
print(sample_predictions)