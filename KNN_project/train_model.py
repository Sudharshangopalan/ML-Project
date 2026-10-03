import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv("crop_recommendation.csv")

print("Dataset loaded successfully!")
print(data.head())


# Input features
features = [
        "Nitrogen",
        "Phosphorus",
        "Potassium",
        "Temperature",
        "Humidity",
        "pH_Value",
        "Rainfall"
    ]

X=data[features]

# Target
y = data["Crop"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create KNN model
knn = KNeighborsClassifier(
    n_neighbors=5
)


# Train model
knn.fit(X_train, y_train)


# Test model
y_pred = knn.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy * 100, "%")


# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# USER INPUT

print("CROP RECOMMENDATION SYSTEM")

try:

    Nitrogen = float(input("Enter Nitrogen (N): "))

    Phosphorus = float(input("Enter Phosphorus (P): "))

    Potassium = float(input("Enter Potassium (K): "))

    Temperature = float(
        input("Enter Temperature (°C): ")
    )

    Humidity = float(
        input("Enter Humidity (%): ")
    )

    pH_Value = float(
        input("Enter Soil pH: ")
    )

    Rainfall = float(
        input("Enter Rainfall (mm): ")
    )


    # Create DataFrame for User Input
    user_input = pd.DataFrame(
        [[
            Nitrogen,
            Phosphorus,
            Potassium,
            Temperature,
            Humidity,
            pH_Value,
            Rainfall
        ]],
        columns=features
    )


    # Predict Crop
    

    prediction = knn.predict(user_input)

    recommended_crop = prediction[0]


    # Display Result

    print(
        "\nRecommended Crop:",
        recommended_crop
    )


except ValueError:

    print("\nInvalid input!")
    print("Please enter numbers only.")

# Save model
with open("crop_knn_model.pkl", "wb") as file:
    pickle.dump(knn, file)

print("\nModel saved as crop_knn_model.pkl")