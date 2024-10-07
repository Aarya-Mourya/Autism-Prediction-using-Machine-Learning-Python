import pandas as pd
import matplotlib.pyplot as plt

# Load adult and toddler data
df_adult = pd.read_csv("/home/aaryamourya/Project-ASD/csvdata/adult_data.csv")
df_toddler = pd.read_csv("/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv")

# Plot Age Distribution
plt.figure(figsize=(10, 6))
plt.plot(df_adult['age'], label='Adults', color='blue')
plt.plot(df_toddler['age'], label='Toddlers', color='orange')
plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Age (years)', fontsize=12)
plt.title('Age Distribution: Adults vs. Toddlers', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('age_distribution.png')
plt.show()

# Plot Gender Distribution
gender_counts_adult = df_adult['gender'].value_counts()
gender_counts_toddler = df_toddler['gender'].value_counts()

fig, ax = plt.subplots(figsize=(8, 6))

bar_width = 0.35
index = range(len(gender_counts_adult))

bar1 = ax.barh(index, gender_counts_adult.values, bar_width, label='Adults', color='blue')
bar2 = ax.barh([i + bar_width for i in index], gender_counts_toddler.values, bar_width, label='Toddlers', color='orange')

ax.set_xlabel('Count', fontsize=12)
ax.set_ylabel('Gender', fontsize=12)
ax.set_title('Gender Distribution: Adults vs. Toddlers', fontsize=14)
ax.set_yticks([i + bar_width / 2 for i in index])
ax.set_yticklabels(gender_counts_adult.index)
ax.legend()

plt.grid(True)
plt.savefig('gender_distribution.png')
plt.show()

# Plot Age vs. Result Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df_adult['age'], df_adult['result'], marker='o', label='Adults', color='blue', alpha=0.7)
plt.scatter(df_toddler['age'], df_toddler['result'], marker='s', label='Toddlers', color='orange', alpha=0.7)
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Result', fontsize=12)
plt.title('Age vs. Result: Adults vs. Toddlers', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('age_vs_result.png')
plt.show()

# Function to create bar plots for categorical variables
def plot_bar_distribution(df_adult, df_toddler, column, title, filename, rotate_labels=False):
    counts_adult = df_adult[column].value_counts()
    counts_toddler = df_toddler[column].value_counts()

    fig, ax = plt.subplots(figsize=(8, 6))

    bar_width = 0.35
    index = range(len(counts_adult))

    bar1 = ax.bar(index, counts_adult.values, bar_width, label='Adults', color='blue')
    bar2 = ax.bar([i + bar_width for i in index], counts_toddler.values, bar_width, label='Toddlers', color='orange')

    ax.set_xlabel('Count', fontsize=12)
    ax.set_ylabel(column, fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(counts_adult.index, rotation=45 if rotate_labels else 0, ha='right')
    ax.legend()

    plt.grid(True)
    plt.tight_layout()  # Adjust layout to make room for rotated labels
    plt.savefig(filename)
    plt.show()

# Function to create pie charts for categorical variables
def plot_pie_distribution(df_adult, df_toddler, column, title, filename):
    counts_adult = df_adult[column].value_counts()
    counts_toddler = df_toddler[column].value_counts()

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].pie(counts_adult, labels=counts_adult.index, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
    ax[0].set_title(f'Adults - {title}')

    ax[1].pie(counts_toddler, labels=counts_toddler.index, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
    ax[1].set_title(f'Toddlers - {title}')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Plot Ethnicity Distribution with rotated labels
plot_bar_distribution(df_adult, df_toddler, 'ethnicity', 'Ethnicity Distribution: Adults vs. Toddlers', 'ethnicity_distribution.png', rotate_labels=True)

# Plot Jundice Distribution
plot_pie_distribution(df_adult, df_toddler, 'jundice', 'Jundice Distribution: Adults vs. Toddlers', 'jundice_distribution.png')

# Plot Used App Before Distribution
fig, ax = plt.subplots(figsize=(8, 6))
counts_adult = df_adult['used_app_before'].value_counts()
counts_toddler = df_toddler['used_app_before'].value_counts()

bar_width = 0.35
index = range(len(counts_adult))

bar1 = ax.barh(index, counts_adult.values, bar_width, label='Adults', color='blue')
bar2 = ax.barh([i + bar_width for i in index], counts_toddler.values, bar_width, label='Toddlers', color='orange')

ax.set_xlabel('Count', fontsize=12)
ax.set_ylabel('Used App Before', fontsize=12)
ax.set_title('Used App Before Distribution: Adults vs. Toddlers', fontsize=14)
ax.set_yticks([i + bar_width / 2 for i in index])
ax.set_yticklabels(counts_adult.index)
ax.legend()

plt.grid(True)
plt.savefig('used_app_before_distribution.png')
plt.show()

# Plot Country of Residence Distribution with rotated labels
plot_bar_distribution(df_adult, df_toddler, 'country_of_residence', 'Country of Residence Distribution: Adults vs. Toddlers', 'country_of_residence_distribution.png', rotate_labels=True)

# Plot Relation Distribution
plot_pie_distribution(df_adult, df_toddler, 'relation', 'Relation Distribution: Adults vs. Toddlers', 'relation_distribution.png')

