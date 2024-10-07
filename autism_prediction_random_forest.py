import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Define file paths
csv_file_path_adult = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv'
csv_file_path_toddler = '/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv'

# Load datasets
adult_df = pd.read_csv(csv_file_path_adult)
toddler_df = pd.read_csv(csv_file_path_toddler)

# Display the first few rows of each dataset to understand their structure
print("Adult Dataset:")
print(adult_df.head())

print("\nToddler Dataset:")
print(toddler_df.head())

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical variables for adults
for column in ['gender', 'ethnicity', 'contry_of_res', 'relation', 'Class/ASD']:
    adult_df[column] = label_encoder.fit_transform(adult_df[column])

# Encode categorical variables for toddlers
for column in ['gender', 'ethnicity', 'contry_of_res', 'relation', 'Class/ASD']:
    toddler_df[column] = label_encoder.fit_transform(toddler_df[column])

# Handle missing values for adults
# Exclude non-numeric columns like 'age_desc' from mean calculation
numeric_columns_adult = adult_df.select_dtypes(include=['number']).columns
adult_df[numeric_columns_adult] = adult_df[numeric_columns_adult].fillna(adult_df[numeric_columns_adult].mean())

# Handle missing values for toddlers
numeric_columns_toddler = toddler_df.select_dtypes(include=['number']).columns
toddler_df[numeric_columns_toddler] = toddler_df[numeric_columns_toddler].fillna(toddler_df[numeric_columns_toddler].mean())

# Display the datasets after preprocessing
print("\nEncoded and Preprocessed Adult Dataset:")
print(adult_df.head())

print("\nEncoded and Preprocessed Toddler Dataset:")
print(toddler_df.head())

# Example of splitting data into training and testing sets
# For demonstration purposes, you may adjust test_size and random_state as needed
X_adult = adult_df.drop('Class/ASD', axis=1)
y_adult = adult_df['Class/ASD']
X_train_adult, X_test_adult, y_train_adult, y_test_adult = train_test_split(X_adult, y_adult, test_size=0.2, random_state=42)

X_toddler = toddler_df.drop('Class/ASD', axis=1)
y_toddler = toddler_df['Class/ASD']
X_train_toddler, X_test_toddler, y_train_toddler, y_test_toddler = train_test_split(X_toddler, y_toddler, test_size=0.2, random_state=42)

# Optionally, you can save the preprocessed datasets to new CSV files if needed
# Example:
# adult_df.to_csv('/home/aaryamourya/Project-ASD/preprocessed_adult_data.csv', index=False)
# toddler_df.to_csv('/home/aaryamourya/Project-ASD/preprocessed_toddler_data.csv', index=False)

# Now, you can proceed with training your Random Forest classifier and evaluating its performance.
# If you need assistance with training and evaluation, feel free to ask!

