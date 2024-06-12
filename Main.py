
import os
import pandas as pd
from DBQuerySelect import DBQuerySelect
from ExcelFile import ExcelFile






if __name__ == "__main__":

    data_folder = 'files'
    # file_name = 'QuestionnaireReader.xlsx'
    # file_path = os.path.join(data_folder, file_name)
    sheet_name = 'QuestionConfiguration'
    # column_name = 'Name'

    # excel_reader = ExcelFile(file_path)
    # excel_reader.read_sheet(sheet_name)
    # questionnaire_name = excel_reader.get_column_values(column_name)


    db_connection = 'postgresql://savodyarkin_n:gsXAww8kIAiz3EVM@172.27.10.11:6432/pharma-demo'
    output_file = os.path.join(data_folder, 'log.xlsx') 
    db_query = DBQuerySelect(db_connection)
    select_data = db_query.select_query(sheet_name)
    if select_data is not None:
        db_query.save_to_excel(select_data, output_file)
        print(f"Data saved to {output_file}")






