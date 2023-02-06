import pathlib
import pandas as pd 

def get_csvs(type):
    parent_path = pathlib.Path(__file__).resolve().parent.parent.parent

    python_filename = 'python_' + type + '_results.csv'
    excel_filename = 'excel_' + type + '_results.csv'
    
    python_path = pathlib.PurePath.joinpath(parent_path, python_filename)
    excel_path = pathlib.PurePath.joinpath(parent_path, excel_filename)

    python_results = pd.read_csv(python_path)
    excel_results = pd.read_csv(excel_path)

    return python_results, excel_results
    