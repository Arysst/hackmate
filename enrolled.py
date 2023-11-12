import pandas as pd

file_path_students_residence = 'Datathon_Students_enrolled_in_bachelors_and_masters_degrees_22-23_place_of_residence_course_V2.xlsx'

students_residence_data = pd.read_excel(file_path_students_residence)

students_residence_data.head()
