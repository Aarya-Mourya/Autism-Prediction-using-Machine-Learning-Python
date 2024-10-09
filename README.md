Here’s a detailed `README.md` file structure for your project in Markdown format:

---

# Autism Spectrum Disorder (ASD) Prediction Using Machine Learning

This project aims to predict Autism Spectrum Disorder (ASD) using machine learning models for both adults and toddlers. By analyzing responses to screening questions, the project leverages Random Forest classifiers to assess ASD risk. Visualizations and performance metrics help in interpreting the models' effectiveness.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Visualization](#visualization)
  - [Age Distribution](#age-distribution)
  - [Gender Distribution](#gender-distribution)
  - [Age vs Result](#age-vs-result)
  - [Ethnicity Distribution](#ethnicity-distribution)
  - [Jundice Distribution](#jundice-distribution)
  - [Used App Before Distribution](#used-app-before-distribution)
- [Machine Learning Model](#machine-learning-model)
  - [Random Forest Classifier](#random-forest-classifier)
  - [Adult Model Performance](#adult-model-performance)
  - [Toddler Model Performance](#toddler-model-performance)
  - [Confusion Matrix Analysis](#confusion-matrix-analysis)
  - [Feature Importance](#feature-importance)
- [Conclusion](#conclusion)
---

## Introduction

Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition. Early diagnosis is crucial for providing timely intervention and support. This project builds machine learning models, specifically Random Forest classifiers, to predict ASD in both adults and toddlers based on responses to a set of screening questions. 

The project also provides a set of visualizations to explore the characteristics of the dataset, as well as the performance of the models.

## Dataset

The dataset includes two parts:
- **Adults:** Consisting of ASD screening results for adults.
- **Toddlers:** Consisting of ASD screening results for toddlers.

Each dataset includes features like:
- **Age**
- **Gender**
- **Ethnicity**
- **Family history of ASD**
- **Screening results**
- **Previous use of the screening app**
- **History of jaundice (Jundice)**

## Visualization

Several visualizations were created to explore the dataset and help understand the distribution and relationships between key features.

### Age Distribution
**Purpose:** To visualize the distribution of ages in the adult and toddler datasets.
![age_distribution](https://github.com/user-attachments/assets/09e9c495-9145-4e29-adaa-08492e0e2d7e)

- **Method:** 
  - Create histograms for adults and toddlers to show the frequency of different age groups.
  - **Annotations:** Add labels, titles, and grid lines for better interpretation.
  - **Saving the Plot:** Save the histogram as `age_distribution.png`.

### Gender Distribution
**Purpose:** To compare the gender distribution between adults and toddlers.
![gender_distribution](https://github.com/user-attachments/assets/9b6f609b-d1af-4c7e-adf7-d30de0c4284f)

- **Method:**
  - Use a horizontal bar plot to represent the count of each gender.
  - **Annotations:** Add labels, titles, and grid lines for better interpretation.
  - **Saving the Plot:** Save the bar chart as `gender_distribution.png`.

### Age vs Result
**Purpose:** To visualize the relationship between age and the screening result for adults and toddlers.
![age_vs_result](https://github.com/user-attachments/assets/0ec25ea7-43fe-410b-aead-aeb8c6b19319)

- **Method:**
  - Create a scatter plot with age on the x-axis and result on the y-axis.
  - **Annotations:** Add labels, titles, and grid lines for better interpretation.
  - **Saving the Plot:** Save the scatter plot as `age_vs_result.png`.

### Ethnicity Distribution
**Purpose:** To analyze the distribution of different ethnicities in the adult and toddler datasets.
![ethnicity_distribution (1)](https://github.com/user-attachments/assets/5c129afc-fcd5-4c2e-a815-9682dbc41722)

- **Method:**
  - Count the occurrences of each ethnicity using `value_counts()`.
  - Create a vertical bar plot with separate bars for adults (blue) and toddlers (orange).
  - Rotate x-axis labels to avoid overlapping.
  - **Annotations:** Add labels, titles, and grid lines for better interpretation.
  - **Saving the Plot:** Save the bar plot as `ethnicity_distribution.png`.
Project tree -
![print asdml 21 (1) pdf-image-005](https://github.com/user-attachments/assets/1a9b5ded-1ed8-459c-b699-188065183284)


### Jundice Distribution
**Purpose:** To analyze the distribution of jaundice history in the adult and toddler datasets.
![jundice_distribution](https://github.com/user-attachments/assets/1c9a15fa-a1e1-4aef-adf2-d697624a6d93)

- **Method:**
  - Count the occurrences of jaundice history (Yes/No).
  - Create separate pie charts for adults and toddlers, each representing the proportion of individuals with or without a history of jaundice.
  - **Annotations:** Add titles to each pie chart segment.
  - **Saving the Plot:** Save the pie charts as `jundice_distribution.png`.

### Used App Before Distribution
**Purpose:** To analyze the distribution of previous app usage in the adult and toddler datasets.
![used_app_before_distribution](https://github.com/user-attachments/assets/ec0561d6-6e5a-4eb7-bd2b-b4aa570d8bcc)

- **Method:**
  - Count the occurrences of previous app usage (Yes/No).
  - Create a horizontal bar plot with separate bars for adults (blue) and toddlers (orange).
  - **Annotations:** Add labels, titles, and grid lines for better interpretation.
  - **Saving the Plot:** Save the bar plot as `used_app_before_distribution.png`.

## Machine Learning Model

### Random Forest Classifier
![print asdml 21 (1) pdf-image-011](https://github.com/user-attachments/assets/9715f953-a04f-4905-9281-e194aeca552f)

The Random Forest classifier is used to predict ASD based on the input data. The classifier was trained separately for adults and toddlers, and its performance was evaluated using standard metrics such as accuracy, precision, recall, and F1 score.

### Adult Model Performance
- **Accuracy:** 86%
- **Precision:** 89%
- **Recall:** 86%

These results show that the model is effective in predicting ASD for the adult population, with strong precision and recall metrics indicating its reliability in identifying true positives and minimizing false negatives.

### Toddler Model Performance
- **Accuracy, Precision, Recall, F1 Score:** 100%

The toddler model achieved perfect results, which may be due to the size and simplicity of the dataset. Further testing is required to confirm the model's robustness in larger and more complex datasets.

### Confusion Matrix Analysis
A confusion matrix was generated for both models, providing deeper insight into their performance by visualizing:
![print asdml 21 (1) pdf-image-020](https://github.com/user-attachments/assets/28ab5e36-9603-464b-8618-0494869fce5a)

- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

This analysis helps identify any potential biases or errors in the model's predictions.

### Feature Importance
Feature importance analysis was conducted to identify which features were most influential in predicting ASD. This analysis can help in understanding key indicators of ASD and may guide future research.

## Conclusion

This project demonstrates the potential of using machine learning, particularly Random Forest classifiers, to predict Autism Spectrum Disorder. The models show promising performance, especially for the toddler dataset. However, more data and testing are required to generalize these findings to broader populations.

Future work includes:
- Refining the models with larger datasets.
- Exploring more complex machine learning algorithms.
- Investigating the implications of feature importance in understanding ASD risk factors.

---
