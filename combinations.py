import pandas as pd

mobility_students_data = pd.read_excel('Datathon_Results_MOBILITY_2022_original_Students.xlsx')

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


def create_combination_string(row):
    stages = [
        str(row['Transport_Stage_1']),
        str(row['Transport_Stage_2']),
        str(row['Transport_Stage_3'])
    ]
    return ' + '.join(filter(lambda x: x != 'nan', stages))


mobility_survey_data['Transport_Combination'] = mobility_survey_data.apply(create_combination_string, axis=1)

combination_counts = mobility_survey_data['Transport_Combination'].value_counts()

combination_counts_df = combination_counts.reset_index()
combination_counts_df.columns = ['Transport_Combination', 'Count']

print(combination_counts_df.head(10))
