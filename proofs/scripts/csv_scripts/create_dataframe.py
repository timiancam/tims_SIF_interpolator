import pandas as pd
from csv_scripts.get_column_names import get_column_names
from csv_scripts.get_input_data import get_input_data
from csv_scripts.get_coefficient_data import get_coefficient_data

def create_dataframe(inputs, interpolated_results):
    column_names = get_column_names()

    data = dict.fromkeys(column_names)

    for key in data:

        if key in ['ac', 'ah', 'hri']:
            data[key] = get_input_data(inputs, key)
        else:
            data[key] = get_coefficient_data(interpolated_results, key)

    dataframe = pd.DataFrame(data=data)

    return dataframe
