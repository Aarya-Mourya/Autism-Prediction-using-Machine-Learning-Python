import pandas as pd
from sklearn.model_selection import train_test_split

# Correct spellings and required columns
required_columns = [
    "A1_Score", "A2_Score", "A3_Score", "A4_Score", "A5_Score",
    "A6_Score", "A7_Score", "A8_Score", "A9_Score", "A10_Score",
    "age", "gender", "ethnicity", "jundice", "contry_of_res",
    "used_app_before", "result", "age_desc", "relation", "Class/ASD"
]

# Paths to the original datasets
adult_data_path = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv'
toddler_data_path = '/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv'

# Paths to save the new training and testing datasets
adult_train_data_path = '/home/aaryamourya/Project-ASD/csvdata/adult_training_data.csv'
adult_test_data_path = '/home/aaryamourya/Project-ASD/csvdata/adult_testing_data.csv'
toddler_train_data_path = '/home/aaryamourya/Project-ASD/csvdata/toddler_training_data.csv'
toddler_test_data_path = '/home/aaryamourya/Project-ASD/csvdata/toddler_testing_data.csv'

# Load the datasets
adult_data = pd.read_csv(adult_data_path)
toddler_data = pd.read_csv(toddler_data_path)

# Ensure datasets have the required columns and correct spelling
adult_data = adult_data[required_columns]
toddler_data = toddler_data[required_columns]

# Ensure each dataset has exactly 50 rows
if len(adult_data) > 50:
    adult_data = adult_data.sample(n=50, random_state=42)
if len(toddler_data) > 50:
    toddler_data = toddler_data.sample(n=50, random_state=42)

# Split the adult data into training and testing sets
adult_train, adult_test = train_test_split(adult_data, test_size=0.2, random_state=42)
adult_train.to_csv(adult_train_data_path, index=False)
adult_test.to_csv(adult_test_data_path, index=False)

# Split the toddler data into training and testing sets
toddler_train, toddler_test = train_test_split(toddler_data, test_size=0.2, random_state=42)
toddler_train.to_csv(toddler_train_data_path, index=False)
toddler_test.to_csv(toddler_test_data_path, index=False)

print("Datasets have been split, corrected, and saved successfully.")

