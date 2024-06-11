
import pandas as pd
from ExcelFile import ExcelFile


file_path = 'QuestionnaireReader.xlsx'
sheet_name = 'Questionnaire'
column_name = 'Name'

excel_reader = ExcelFile(file_path)
excel_reader.read_sheet(sheet_name)
questionnaire_name = excel_reader.get_column_values(column_name)

for name in questionnaire_name:
    print(name)

print(questionnaire_name)

print(len(questionnaire_name))




# excel_file('Обратиться к вкладке 1')
# excel_file('Обратиться к вкладке 2')





