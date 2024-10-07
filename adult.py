import pandas as pd

# Define the data for adults
adult_data = {
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
    'age': [25, 30, 28, 35, 32, 40, 22, 27, 38, 45, 29, 33, 31, 26, 39, 41, 36, 34, 24, 37, 30, 25, 32, 40, 29],
    'gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
    'ethnicity': ['White-European', 'Asian', 'Latino', 'Others', 'Black', 'Middle Eastern', 'South Asian', 'Hispanic', 'Native American', 'Pacific Islander', 'White-European', 'Asian', 'Latino', 'Others', 'Black', 'Middle Eastern', 'South Asian', 'Hispanic', 'Native American', 'Pacific Islander', 'White-European', 'Asian', 'Latino', 'Others', 'Black'],
    'jundice': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'austim': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'contry_of_res': ['UK', 'USA', 'Canada', 'Australia', 'France', 'Germany', 'Spain', 'Italy', 'India', 'China', 'Japan', 'Russia', 'Brazil', 'South Africa', 'Egypt', 'Mexico', 'Netherlands', 'Sweden', 'Norway', 'Finland', 'Denmark', 'Belgium', 'Ireland', 'Switzerland', 'Austria'],
    'used_app_before': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'result': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'age_desc': ['18 and more'] * 25,
    'relation': ['Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent', 'Self', 'Parent', 'Relative', 'Others', 'Parent'],
    'Class/ASD': ['YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
}

# Create DataFrame for adults
df_adults = pd.DataFrame(adult_data)

# Save to CSV
csv_file_path_adults = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv'
df_adults.to_csv(csv_file_path_adults, index=False)
print(f"Adult CSV file saved to: {csv_file_path_adults}")

