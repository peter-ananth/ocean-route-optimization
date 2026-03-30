import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# load dataset
data = pd.read_csv("dataset/marine_data.csv")

# features
X = data[[
    "wind_speed",
    "wave_height",
    "pressure",
    "current_speed",
    "visibility"
]]

# target
y = data["safe"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# train model
model.fit(X_train, y_train)

# accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# save model
joblib.dump(model, "model/marine_model.pkl")

print("Model saved successfully!")
