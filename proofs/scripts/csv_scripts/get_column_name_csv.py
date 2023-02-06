import pathlib

def get_column_name_csv():
    root_path = pathlib.Path(__file__).resolve().parent
    csv = pathlib.PurePath.joinpath(root_path, 'column_names.csv')

    return csv
    