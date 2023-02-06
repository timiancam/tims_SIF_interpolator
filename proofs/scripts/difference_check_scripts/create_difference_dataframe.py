import pandas as pd
from difference_check_scripts.find_difference import find_difference

def create_difference_dataframe(python_results, excel_results):

    data = {}

    for column in python_results:
        data[column + '_difference'] = find_difference(python_results, excel_results, column)

    dataframe = pd.DataFrame(data=data)

    return dataframe
