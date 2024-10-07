import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load adult dataset
csv_file_path_adult = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv'
adult_df = pd.read_csv(csv_file_path_adult)

# Load toddler dataset
csv_file_path_toddler = '/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv'
toddler_df = pd.read_csv(csv_file_path_toddler)

# Encode categorical variables
encoder = LabelEncoder()

# Adult dataset encoding
for column in ['gender', 'ethnicity', 'contry_of_res', 'relation', 'Class/ASD']:
    adult_df[column] = encoder.fit_transform(adult_df[column])

# Toddler dataset encoding
for column in ['gender', 'ethnicity', 'contry_of_res', 'relation', 'Class/ASD']:
    toddler_df[column] = encoder.fit_transform(toddler_df[column])

# Splitting the Adult Dataset
X_adult = adult_df.drop(columns=['Class/ASD'])
y_adult = adult_df['Class/ASD']
X_train_adult, X_test_adult, y_train_adult, y_test_adult = train_test_split(X_adult, y_adult, test_size=0.2, random_state=42)

# Splitting the Toddler Dataset
X_toddler = toddler_df.drop(columns=['Class/ASD'])
y_toddler = toddler_df['Class/ASD']
X_train_toddler, X_test_toddler, y_train_toddler, y_test_toddler = train_test_split(X_toddler, y_toddler, test_size=0.2, random_state=42)

# Print dataset shapes after splitting
print(f"Shapes after splitting:")
print(f"Adult Train/Test: {X_train_adult.shape} {X_test_adult.shape}")
print(f"Toddler Train/Test: {X_train_toddler.shape} {X_test_toddler.shape}")

