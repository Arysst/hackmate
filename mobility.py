import pandas as pd

file_path_mobility_students = 'Datathon_Results_MOBILITY_2022_original_Students.xlsx'

mobility_students_data = pd.read_excel(file_path_mobility_students)

mobility_students_data.head()
