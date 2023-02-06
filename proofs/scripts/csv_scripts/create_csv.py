import pathlib
from csv_scripts.create_dataframe import create_dataframe

def create_csv(inputs, interpolated_results, file_name):
    dataframe = create_dataframe(inputs, interpolated_results)

    parent_path = pathlib.Path(__file__).resolve().parent.parent.parent
    path = pathlib.PurePath.joinpath(parent_path, file_name)
    dataframe.to_csv(path, index=False)
