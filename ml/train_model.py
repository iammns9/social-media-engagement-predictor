import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

#Loading Dataset
DATASET_PATH = "../dataset/synthetic_social_media_engagement.csv"

print("Loading dataset...")
df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

#Feature Engineering
#Counting hashtags
df["hashtag_count"] = (
    df["hashtags"]
    .fillna("")
    .astype(str)
    .apply(lambda x: 0 if x.strip() == "" else len(x.split()))
)

#Removing Unnecessary Columns
columns_to_drop = [
    "post_id",
    "user_id",
    "user_name",
    "post_content",
    "hashtags",
    "account_creation_date",
    "post_date"
]
df.drop(columns=columns_to_drop, inplace=True)

#Features & Target Columns
TARGET = "engagement_rate"

X = df.drop(TARGET, axis=1)
y = df[TARGET]

#Feature Types
categorical_features = [
    "user_gender",
    "location",
    "topic",
    "device",
    "language"
]

numeric_features = [
    "user_age",
    "followers_count",
    "following_count",
    "content_length",
    "likes",
    "comments",
    "shares",
    "hashtag_count"
]

boolean_features = [
    "is_verified",
    "has_media"
]

#Converting True/False → 1/0
for col in boolean_features:
    X[col] = X[col].astype(int)
numeric_features.extend(boolean_features)

#Preprocessing
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

#Random Forest Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

#Training / Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining model...")
pipeline.fit(X_train, y_train)
print("Training Completed!")

#Evaluation
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")
print(f"MAE       : {mae:.6f}")
print(f"MSE       : {mse:.6f}")
print(f"RMSE      : {rmse:.6f}")
print(f"R² Score  : {r2:.4f}")
print("==============================")

#Model Saving
BACKEND_FOLDER = "../backend"
os.makedirs(BACKEND_FOLDER, exist_ok=True)

MODEL_PATH = os.path.join(BACKEND_FOLDER, "engagement_model.pkl")
joblib.dump(pipeline, MODEL_PATH)
print("\nModel Saved Successfully!")
print(f"Location: {MODEL_PATH}")