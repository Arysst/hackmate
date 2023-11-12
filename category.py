import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

file_path_mobility_students = 'Datathon_Results_MOBILITY_2022_original_Students.xlsx'

mobility_students_data = pd.read_excel(file_path_mobility_students)

mobility_students_data.head()

mobility_columns = [
    'Select the center where you study:',
    'How many days per week do you usually come to the university?',
    'Please indicate the postal code from where you usually start your trip to the university:',
    'Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 1]',
    'Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 2]',
    'Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 3]'
]
mobility_survey_data = mobility_students_data[mobility_columns]

mobility_survey_data.columns = [
    'Study_Center', 'Days_Per_Week', 'Postal_Code',
    'Transport_Stage_1', 'Transport_Stage_2', 'Transport_Stage_3'
]

transport_modes = ['Walking', 'Bicycle', 'Public transport', 'Car', 'Motorcycle', 'Other']
transport_counts = {mode: 0 for mode in transport_modes}

for mode in transport_modes:
    for stage in ['Transport_Stage_1', 'Transport_Stage_2', 'Transport_Stage_3']:
        transport_counts[mode] += mobility_survey_data[stage].str.contains(mode, case=False, na=False).sum()

transport_counts_df = pd.DataFrame(list(transport_counts.items()), columns=['Transportation_Mode', 'Student_Count'])
transport_counts_df.sort_values('Student_Count', ascending=False, inplace=True)
transport_counts_df.reset_index(drop=True, inplace=True)

categories = {
    'Active Mobility': ['On foot', 'Bicycle'],
    'Public Transportation': ['Underground', 'Bus', 'Renfe', 'FGC', 'Tram'],
    'Private Transportation': [
        'Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable source charging),',
        'Combustion or electric motorcycle with non-renewable source charging',
        'Scooter (or other micro-mobility devices) with renewable charging',
        'Electric vehicle (with Zero label and renewable source charging)',
        'Scooter (or other micro-mobility devices) with non-renewable charging',
        'Electric motorcycle',
        'Taxi'
    ]
}

mobility_survey_data['Category'] = 'Other'
for category, modes in categories.items():
    for mode in modes:
        for stage in ['Transport_Stage_1', 'Transport_Stage_2', 'Transport_Stage_3']:
            mobility_survey_data.loc[
                mobility_survey_data[stage].str.contains(mode, case=False, na=False), 'Category'] = category

category_counts = mobility_survey_data['Category'].value_counts().reset_index()
category_counts.columns = ['Transportation_Category', 'Student_Count']
category_counts.sort_values('Student_Count', ascending=False, inplace=True)
category_counts.reset_index(drop=True, inplace=True)
print(category_counts)

plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Transportation_Category', y='Student_Count', data=category_counts, palette='viridis')

plt.title('UPC Students Daily Commute by Transportation Category', fontsize=15)
plt.xlabel('Transportation Category', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)

for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'),
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center',
                     xytext=(0, 9),
                     textcoords='offset points')

plt.show()
