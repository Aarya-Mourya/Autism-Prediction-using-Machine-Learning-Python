import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Specify full file paths
csv_file_adult = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv'
csv_file_toddler = '/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv'

# Load data
df_adult = pd.read_csv(csv_file_adult)
df_toddler = pd.read_csv(csv_file_toddler)

# Handle missing values (fill with mean for numerical features)
numerical_features_adult = df_adult.select_dtypes(include=['float64', 'int64']).columns
numerical_features_toddler = df_toddler.select_dtypes(include=['float64', 'int64']).columns

df_adult[numerical_features_adult] = df_adult[numerical_features_adult].fillna(df_adult[numerical_features_adult].mean())
df_toddler[numerical_features_toddler] = df_toddler[numerical_features_toddler].fillna(df_toddler[numerical_features_toddler].mean())

# Encode categorical features
le = LabelEncoder()
categorical_features_adult = df_adult.select_dtypes(include=['object']).columns
categorical_features_toddler = df_toddler.select_dtypes(include=['object']).columns

for col in categorical_features_adult:
    df_adult[col] = le.fit_transform(df_adult[col])

for col in categorical_features_toddler:
    df_toddler[col] = le.fit_transform(df_toddler[col])

# Feature scaling
scaler = StandardScaler()
df_adult[numerical_features_adult] = scaler.fit_transform(df_adult[numerical_features_adult])
df_toddler[numerical_features_toddler] = scaler.fit_transform(df_toddler[numerical_features_toddler])

# Separate features and target variables
X_train_adult, X_test_adult, y_train_adult, y_test_adult = train_test_split(
    df_adult.drop("Class/ASD", axis=1), df_adult["Class/ASD"], test_size=0.2, random_state=42
)

X_train_toddler, X_test_toddler, y_train_toddler, y_test_toddler = train_test_split(
    df_toddler.drop("Class/ASD", axis=1), df_toddler["Class/ASD"], test_size=0.2, random_state=42
)

# Train models
clf_adult = RandomForestClassifier(n_estimators=100, random_state=42)
clf_toddler = RandomForestClassifier(n_estimators=100, random_state=42)

clf_adult.fit(X_train_adult, y_train_adult)
clf_toddler.fit(X_train_toddler, y_train_toddler)

# Evaluation function
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)

    print("Model Performance:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print("\nConfusion Matrix:\n", cm)

# Evaluate models
print("Adult Model Performance:")
evaluate_model(clf_adult, X_test_adult, y_test_adult)

print("\nToddler Model Performance:")
evaluate_model(clf_toddler, X_test_toddler, y_test_toddler)

