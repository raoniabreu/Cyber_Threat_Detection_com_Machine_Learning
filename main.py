import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load dataset
data = pd.read_csv("data/KDDTrain+.txt", header=None)

# Separate features and target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Convert categorical features into numerical (one-hot encoding)
X = pd.get_dummies(X)

# Ensure all column names are strings (required by scikit-learn)
X.columns = X.columns.astype(str)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Define models to compare
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC()
}

results = {}

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

    print(f"\nModel: {name}")
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Save results to file
with open("results.txt", "w") as f:
    for name, acc in results.items():
        f.write(f"{name}: {acc:.4f}\n")

# Plot model comparison
plt.bar(results.keys(), results.values())
plt.title("Model Comparison")
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.savefig("model_comparison.png")
plt.show()