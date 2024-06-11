import pandas as pd


class ExcelFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_sheet(self, sheet_name):
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=sheet_name)
        except Exception as e:
            print(f"Error reading excel file")

    
    def get_column_values(self, column_name):
        if self.data is not None:
            if column_name in self.data.columns:
                return self.data[column_name].tolist()
            else:
                print(f"Column {column_name} do not exists")
                return 0



    # def print_data(self):
    #     if self.questionnaire_name:
    #             for name in self.questionnaire_name:
    #                 print(name)
    #     else:
    #         print("No data")