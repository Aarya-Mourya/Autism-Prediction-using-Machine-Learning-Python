import tkinter as tk
from tkinter import ttk
import pandas as pd

# Define options for dropdowns
ethnicity_options = ["White-European", "Asian", "Latino", "Others", "Black", "Middle Eastern", "South Asian"]
country_options = ["UK", "USA", "Canada", "Australia", "France", "Germany", "Spain","India", "Other"]
relation_options = ["Self", "Parent", "Relative", "Others"]

# Contact information based on country
country_contacts = {
    "UK": "Contact UK support at +44-123-456-7890",
    "USA": "Contact USA support at +1-800-123-4567",
    "Canada": "Contact Canada support at +1-877-987-6543",
    "Australia": "Contact Australia support at +61-1800-987-654",
    "France": "Contact France support at +33-1-23-45-67-89",
    "Germany": "Contact Germany support at +49-123-456-7890",
    "Spain": "Contact Spain support at +34-91-234-5678",
    "India": "Contact India support at +91-915-234-5678",
    "Other": "Contact global support at asd@helpline.com"
}

# Questions for adults and toddlers
adult_questions = [
    "I often notice small sounds when others do not.",
    "I usually concentrate more on the whole picture rather than the small details.",
    "I find it easy to do more than one thing at once.",
    "If there is an interruption, I can switch back to what I was doing very quickly.",
    "I find it easy to read between the lines when someone is talking to me.",
    "I know how to tell if someone listening to me is getting bored.",
    "When I'm reading a story I find it difficult to work out the character's intentions.",
    "I like to collect information about categories of things.",
    "I find it easy to work out what someone is thinking or feeling just by looking at their face.",
    "I find it difficult to work out people's intentions."
]

toddler_questions = [
    "S/he often notices small sounds when others do not.",
    "S/he usually concentrates more on the whole picture rather than the small details.",
    "In a social group, s/he can easily keep track of several different people's conversations.",
    "S/he finds it easy to go back and forth if there is an interruption; s/he can switch between different activities.",
    "S/he doesn't know how to keep a conversation going with his/her peers.",
    "S/he is good at social chit-chat.",
    "When s/he is read a story, s/he finds it difficult to work out the character's intentions or feelings.",
    "When s/he was in preschool, s/he used to enjoy playing pretending games with other children.",
    "S/he finds it easy to work out what someone is thinking or feeling just by looking at their face.",
    "S/he finds it hard to make new friends."
]

# Function to handle form submission
def submit_form():
    age_value = age_entry.get()
    category_value = category_var.get()
    gender_value = gender_var.get()
    ethnicity_value = ethnicity_var.get()
    jundice_value = 1 if jundice_var.get() == "Yes" else 0
    country_value = country_var.get()
    used_app_value = 1 if used_app_var.get() == "Yes" else 0
    relation_value = relation_var.get()
    
    # Collecting answers to the questions
    answers = [
        1 if yesno_var1.get() == "Yes" else 0,
        1 if yesno_var2.get() == "Yes" else 0,
        1 if yesno_var3.get() == "Yes" else 0,
        1 if yesno_var4.get() == "Yes" else 0,
        1 if yesno_var5.get() == "Yes" else 0,
        1 if yesno_var6.get() == "Yes" else 0,
        1 if yesno_var7.get() == "Yes" else 0,
        1 if yesno_var8.get() == "Yes" else 0,
        1 if yesno_var9.get() == "Yes" else 0,
        1 if yesno_var10.get() == "Yes" else 0
    ]
    
    # Determine ASD prediction based on scores
    total_score = sum(answers)
    if total_score >= 5:
        asd_result = 1
        asd_class = "YES"
        autism_value = 1
    else:
        asd_result = 0
        asd_class = "NO"
        autism_value = 0

    # Determine the CSV path based on category
    csv_path = '/home/aaryamourya/Project-ASD/csvdata/adult_data.csv' if category_value == "Adult" else '/home/aaryamourya/Project-ASD/csvdata/toddler_data.csv'

    # Create DataFrame and append to CSV
    df = pd.DataFrame([{
        'A1_Score': answers[0], 'A2_Score': answers[1], 'A3_Score': answers[2], 'A4_Score': answers[3],
        'A5_Score': answers[4], 'A6_Score': answers[5], 'A7_Score': answers[6], 'A8_Score': answers[7],
        'A9_Score': answers[8], 'A10_Score': answers[9], 'age': age_value, 'gender': gender_value,
        'ethnicity': ethnicity_value, 'jundice': jundice_value,
        'contry_of_res': country_value, 'used_app_before': used_app_value, 'result': asd_result,
        'age_desc': '4-11 years', 'relation': relation_value, 'Class/ASD': asd_class, 'autism': autism_value
    }])
    df.to_csv(csv_path, mode='a', header=False, index=False)

    # Clear form fields
    age_entry.delete(0, tk.END)
    gender_var.set('')
    ethnicity_var.set('')
    jundice_var.set('')
    country_var.set('')
    used_app_var.set('')
    relation_var.set('')
    for var in [yesno_var1, yesno_var2, yesno_var3, yesno_var4, yesno_var5,
                yesno_var6, yesno_var7, yesno_var8, yesno_var9, yesno_var10]:
        var.set('Yes')

    # Display ASD prediction result on a new page
    new_window = tk.Toplevel(root)
    new_window.title("Result")
    result_message = "Thank you! The person might have ASD." if asd_result == 1 else "Thank you! The person might not have ASD."
    result_label = tk.Label(new_window, text=result_message, font=('Helvetica', 16))
    result_label.pack(padx=20, pady=20)

    # Display contact information based on selected country
    contact_info = country_contacts.get(country_value, "Contact global support at support@example.com")
    contact_label = tk.Label(new_window, text=contact_info)
    contact_label.pack(padx=20, pady=10)
    
    # Schedule closing the form after 30 seconds
    root.after(30000, root.quit)

# Creating main application window
root = tk.Tk()
root.title("Autism Prediction Form")

# Labels and entry fields
category_label = tk.Label(root, text="Category (Adult/Toddler):")
category_label.grid(row=0, column=0, padx=10, pady=5)
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Adult", "Toddler"], state="readonly")
category_dropdown.grid(row=0, column=1, padx=10, pady=5)
category_dropdown.current(0)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["M", "F"], state="readonly")
gender_dropdown.grid(row=2, column=1, padx=10, pady=5)

ethnicity_label = tk.Label(root, text="Ethnicity:")
ethnicity_label.grid(row=3, column=0, padx=10, pady=5)
ethnicity_var = tk.StringVar()
ethnicity_dropdown = ttk.Combobox(root, textvariable=ethnicity_var, values=ethnicity_options, state="readonly")
ethnicity_dropdown.grid(row=3, column=1, padx=10, pady=5)

jundice_label = tk.Label(root, text="Jundice (Yes/No):")
jundice_label.grid(row=4, column=0, padx=10, pady=5)
jundice_var = tk.StringVar()
jundice_dropdown = ttk.Combobox(root, textvariable=jundice_var, values=["Yes", "No"], state="readonly")
jundice_dropdown.grid(row=4, column=1, padx=10, pady=5)

country_label = tk.Label(root, text="Country of Residence:")
country_label.grid(row=5, column=0, padx=10, pady=5)
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(root, textvariable=country_var, values=country_options, state="readonly")
country_dropdown.grid(row=5, column=1, padx=10, pady=5)

used_app_label = tk.Label(root, text="Used App Before (Yes/No):")
used_app_label.grid(row=6, column=0, padx=10, pady=5)
used_app_var = tk.StringVar()
used_app_dropdown = ttk.Combobox(root, textvariable=used_app_var, values=["Yes", "No"], state="readonly")
used_app_dropdown.grid(row=6, column=1, padx=10, pady=5)

relation_label = tk.Label(root, text="Relation:")
relation_label.grid(row=7, column=0, padx=10, pady=5)
relation_var = tk.StringVar()
relation_dropdown = ttk.Combobox(root, textvariable=relation_var, values=relation_options, state="readonly")
relation_dropdown.grid(row=7, column=1, padx=10, pady=5)

# Question labels and dropdowns
yesno_var1 = tk.StringVar(value="Yes")
yesno_var2 = tk.StringVar(value="Yes")
yesno_var3 = tk.StringVar(value="Yes")
yesno_var4 = tk.StringVar(value="Yes")
yesno_var5 = tk.StringVar(value="Yes")
yesno_var6 = tk.StringVar(value="Yes")
yesno_var7 = tk.StringVar(value="Yes")
yesno_var8 = tk.StringVar(value="Yes")
yesno_var9 = tk.StringVar(value="Yes")
yesno_var10 = tk.StringVar(value="Yes")

questions_vars = [
    yesno_var1, yesno_var2, yesno_var3, yesno_var4, yesno_var5,
    yesno_var6, yesno_var7, yesno_var8, yesno_var9, yesno_var10
]

def update_questions(*args):
    if category_var.get() == "Adult":
        questions = adult_questions
    else:
        questions = toddler_questions
    
    for idx, question in enumerate(questions):
        question_labels[idx].config(text=question)

question_labels = []
for i in range(10):
    question_label = tk.Label(root, text="")
    question_label.grid(row=8+i, column=0, padx=10, pady=5)
    question_labels.append(question_label)
    question_dropdown = ttk.Combobox(root, textvariable=questions_vars[i], values=["Yes", "No"], state="readonly")
    question_dropdown.grid(row=8+i, column=1, padx=10, pady=5)

category_var.trace("w", update_questions)
update_questions()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=18, columnspan=2, pady=10)

# Start the application
root.mainloop()

