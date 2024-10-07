import os
import pandas as pd

# Define the directory path for CSV files
csv_dir = '/home/aaryamourya/Project-ASD/csvdata/'

# Create the directory if it doesn't exist
os.makedirs(csv_dir, exist_ok=True)

# Define the data for toddlers
toddler_data = {
    'A1_Score': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'A2_Score': [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    'A3_Score': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'A4_Score': [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    'A5_Score': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'A6_Score': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'A7_Score': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'A8_Score': [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    'A9_Score': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'A10_Score': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    'age': [3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6, 3],
    'gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
    'ethnicity': ['White-European', 'Asian', 'Latino', 'Others', 'Black', 'Middle Eastern', 'South Asian', 'Hispanic', 'Native American', 'Pacific Islander', 'White-European', 'Asian', 'Latino', 'Others', 'Black', 'Middle Eastern', 'South Asian', 'Hispanic', 'Native American', 'Pacific Islander', 'White-European', 'Asian', 'Latino', 'Others', 'Black'],
    'jundice': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'austim': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'contry_of_res': ['UK', 'USA', 'Canada', 'Australia', 'France', 'Germany', 'Spain', 'Italy', 'India', 'China', 'Japan', 'Russia', 'Brazil', 'South Africa', 'Egypt', 'Mexico', 'Netherlands', 'Sweden', 'Norway', 'Finland', 'Denmark', 'Belgium', 'Ireland', 'Switzerland', 'Austria'],
    'used_app_before': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'result': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'age_desc': ['4-11 years'] * 25,
    'relation': ['Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent'],
    'Class/ASD': ['YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
}

# Create DataFrame for toddlers
df_toddlers = pd.DataFrame(toddler_data)

# Save to CSV
csv_file_path_toddlers = os.path.join(csv_dir, 'toddler_data.csv')
df_toddlers.to_csv(csv_file_path_toddlers, index=False)
print(f"Toddler CSV file saved to: {csv_file_path_toddlers}")

